javascript:(function(){
  const PROFILE = {
    firstName: "Brian",
    lastName: "",
    fullName: "Brian",
    email: "Brian.j1274@gmail.com",
    phone: "(707) 596-8503",
    location: "San Francisco, CA 94122",
    address: "21st Ave & Judah St, San Francisco, CA 94122",
    workAuth: "Authorized to work in US, no sponsorship",
    howHeard: "Company website",
    education: "UC Santa Cruz — B.S. Chemistry 2007-2011 — Research Assistant Yat Li Lab (GaN CVD) — Publication ACS J Med Chem Feb 2011",
    experience: "Lab Assistant Quintara Biosciences Jan-May 2012 GLP sample prep QC; Lab Intern MicroConstants Aug-Dec 2011 extraction chromatography spectroscopy; Summer Med Chem Intern Threshold Jun-Aug 2011 organic synthesis HPLC NMR",
    skills: "HPLC, Spectroscopy (NMR, UV-Vis), Chromatography, Sample Prep, QC & Data Analysis, GLP, MS Office, Buffer Prep, Titration, Instrument Maintenance, Electronic Lab Records / LIMS-style",
    salary: "Per posting range / negotiable",
    startDate: "Short notice / 2 weeks"
  };
  function fill(){
    const map = {
      'firstName|first_name|givenName': PROFILE.firstName,
      'lastName|last_name|familyName': PROFILE.lastName,
      'fullName|name': PROFILE.fullName,
      'email': PROFILE.email,
      'phone|tel': PROFILE.phone,
      'location|city|address': PROFILE.location,
      'workAuth|authorization|sponsorship': PROFILE.workAuth,
      'how.*heard|source': PROFILE.howHeard,
      'salary|compensation': PROFILE.salary,
      'startDate|availability': PROFILE.startDate
    };
    let filled=0;
    document.querySelectorAll('input, textarea, select').forEach(el=>{
      const key = (el.name+' '+el.id+' '+el.placeholder+' '+el.getAttribute('aria-label')).toLowerCase();
      for(const pat in map){
        const re = new RegExp(pat,'i');
        if(re.test(key) && !el.value){
          el.focus();
          el.value = map[pat];
          el.dispatchEvent(new Event('input',{bubbles:true}));
          el.dispatchEvent(new Event('change',{bubbles:true}));
          filled++;
          break;
        }
      }
    });
    alert('JobSearchSF Bookmarklet: attempted fill '+filled+' fields. Review before submit! ATS does NOT detect autofill.');
  }
  fill();
})();
