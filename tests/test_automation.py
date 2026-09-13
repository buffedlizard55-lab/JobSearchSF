import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from automation.audit import (assess, audit, board, fetch, normalize, profile_audit,
                              public_url, render, SafeRedirect)


class AuditTests(unittest.TestCase):
    def test_board_exact_host_and_https(self):
        self.assertEqual(board('https://jobs.lever.co/demo/123'), ('lever', 'demo'))
        self.assertIsNone(board('https://jobs.lever.co.evil.example/demo'))
        self.assertIsNone(board('http://jobs.lever.co/demo'))
        self.assertIsNone(board('https://jobs.lever.co/'))

    def test_greenhouse_normalization_excludes_prospects(self):
        rows = list(normalize('greenhouse', 'demo', {'jobs': [
            {'id': 1, 'internal_job_id': None},
            {'id': 2, 'title': 'Lab technician', 'absolute_url': 'https://example.org/jobs/2',
             'location': {'name': 'San Francisco'}, 'content': '<p>HPLC &amp; QC</p>'}]}))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['description'], 'HPLC & QC')
        self.assertEqual(rows[0]['key'], 'greenhouse:demo:2')

    def test_lever_requirements_included(self):
        row = list(normalize('lever', 'demo', [{'id': 'a', 'text': 'RA',
            'hostedUrl': 'https://jobs.lever.co/demo/a', 'lists': [{'content': 'HPLC'}]}]))[0]
        self.assertIn('HPLC', row['description'])

    def test_ashby_unlisted_excluded(self):
        self.assertEqual(list(normalize('ashby', 'demo', {'jobs': [{'isListed': False}]})), [])

    def test_skill_match_never_ready(self):
        job = {'title': 'Lab assistant', 'description': 'HPLC and chromatography',
               'location': 'San Francisco'}
        result = assess(job)
        self.assertEqual(result['triage'], 'potential_match')
        self.assertEqual(result['state'], 'blocked')
        self.assertIn('EMPLOYER_ATS_RELATIONSHIP_UNVERIFIED', result['flags'])

    def test_south_sf_is_not_sf(self):
        self.assertFalse(assess({'title': 'HPLC', 'description': '',
                                 'location': 'South San Francisco'})['sf_location_text'])

    def test_unknown_remote_not_assumed_eligible(self):
        self.assertEqual(assess({'title': 'HPLC', 'description': '',
                                'location': 'Remote'})['triage'], 'not_shortlisted')

    def test_profile_redacted_and_sensitive_unknown(self):
        rows = profile_audit({'personal': {'lastName': '', 'email': 'secret@example.com'},
                              'commonATSAnswers': {'veteran': 'No'}})
        self.assertEqual(rows[0]['flag'], 'MISSING')
        self.assertNotIn('secret@example.com', json.dumps(rows))
        self.assertEqual(rows[-1]['flag'], 'DO_NOT_AUTOFILL_WITHOUT_PRIMARY_EVIDENCE')

    def test_private_destinations_rejected(self):
        with patch('socket.getaddrinfo', return_value=[(None, None, None, None, ('127.0.0.1', 443))]):
            with self.assertRaises(ValueError):
                public_url('https://example.com')

    def test_invalid_urls_rejected(self):
        for url in ['file:///etc/passwd', 'http://example.com', 'https://user:pass@example.com',
                    'https://example.com:8000']:
            with self.assertRaises(ValueError):
                public_url(url)

    def test_redirect_private_destination_rejected(self):
        with patch('automation.audit.public_url', side_effect=ValueError('private')):
            with self.assertRaises(ValueError):
                SafeRedirect().redirect_request(None, None, 302, '', {}, 'https://127.0.0.1')

    def test_fetch_errors_are_not_closed_jobs(self):
        with patch('automation.audit.public_url', side_effect=ValueError('blocked')):
            result = fetch('https://example.org')
        self.assertIsNone(result['status'])
        self.assertIn('error', result)

    def test_offline_all_rows_and_html_escaping(self):
        report = audit(False)
        self.assertEqual(report['summary']['legacy_entries'], 120)
        self.assertEqual(report['applications_submitted'], 0)
        self.assertFalse(report['submission_enabled'])
        report['legacy_audit'][0]['company'] = '<script>alert(1)</script>'
        rendered = render(report)
        self.assertNotIn('<script>alert(1)</script>', rendered)
        self.assertIn('&lt;script&gt;', rendered)

    def test_mocked_live_discovery_and_dedup(self):
        def fake_fetch(url):
            base = {'url': url, 'status': 200, 'checked_at': '2026-09-12T00:00:00+00:00',
                    'sha256': 'test', 'final_url': url}
            if 'boards-api.greenhouse.io' in url:
                payload = {'jobs': [{'id': 1, 'title': 'HPLC Lab assistant',
                    'location': {'name': 'San Francisco'}, 'content': 'HPLC',
                    'absolute_url': 'https://example.org/job/1'}] * 2}
                return dict(base, body=json.dumps(payload))
            if 'api.lever.co' in url:
                return dict(base, body='[]')
            if 'api.ashbyhq.com' in url:
                return dict(base, body='{"jobs": []}')
            return dict(base, body='<a href="https://job-boards.greenhouse.io/biohub">Jobs</a>')
        with patch('automation.audit.fetch', side_effect=fake_fetch):
            report = audit(True)
        keys = [j['key'] for j in report['queue']]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertGreater(report['summary']['potential_matches'], 0)
        self.assertTrue(all(j['state'] == 'blocked' for j in report['queue']))


if __name__ == '__main__':
    unittest.main()
