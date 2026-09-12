// JobSearchSF Easy Apply content script — draft
const PROFILE = {
  firstName: "Brian",
  email: "Brian.j1274@gmail.com",
  phone: "(707) 596-8503",
  location: "San Francisco, CA 94122",
  address: "21st Ave & Judah St, San Francisco, CA 94122",
  workAuth: "Authorized to work in US, no sponsorship",
  howHeard: "Company website"
};
function autofill(){
  const map = {
    'firstName|first_name': PROFILE.firstName,
    'email': PROFILE.email,
    'phone': PROFILE.phone,
    'location|city': PROFILE.location
  };
  let n=0;
  document.querySelectorAll('input, textarea').forEach(el=>{
    const k = (el.name+' '+el.id).toLowerCase();
    for(const pat in map){
      if(new RegExp(pat,'i').test(k) && !el.value){
        el.value = map[pat];
        el.dispatchEvent(new Event('input',{bubbles:true}));
        n++;
        break;
      }
    }
  });
  return n;
}
chrome.runtime.onMessage.addListener((msg, sender, sendResponse)=>{
  if(msg.action==='autofill'){
    const c = autofill();
    sendResponse({filled:c});
  }
});
