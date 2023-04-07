chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var currentTab = tabs[0];
    chrome.tabs.sendMessage(currentTab.id, { message: 'getHeadline' }, function(response) {
      if (response && response.headline) {
        document.getElementById('status').textContent = response.headline;
      } else {
        document.getElementById('status').textContent = 'No article selected.';
      }
    });
  });
  
  document.getElementById('checkBtn').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var currentTab = tabs[0];
      chrome.tabs.sendMessage(currentTab.id, { message: 'checkHeadline' }, function(response) {
        if (response && response.result) {
          document.getElementById('status').textContent = response.result;
        } else {
          document.getElementById('status').textContent = 'Could not check headline.';
        }
      });
    });
  });