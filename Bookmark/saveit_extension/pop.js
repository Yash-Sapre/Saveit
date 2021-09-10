
async function getCurrentTab() {
  let queryOptions = { active: true, currentWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  return tab;
};

getCurrentTab().then((result) => {
  document.getElementById('name').innerText = result.title;
  document.getElementById('url').innerText = result.url;
  fetch('http://127.0.0.1:8000/saveit/api/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: document.getElementById('name').innerText,
    url: document.getElementById('url').innerText,
  })
}).then(res => res.json() )
  .then(data => console.log(data))
  .catch(error => console.log(error));


});







