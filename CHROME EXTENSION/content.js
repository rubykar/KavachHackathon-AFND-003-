chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request && request.message === 'getHeadline') {
      var headline = null;
      // code to get the headline from the page
      sendResponse({ headline: headline });
    } else if (request && request.message === 'checkHeadline') {
      var selectedText = window.getSelection().toString();
      var result = null;
      // code to analyze the selected text with the model
      sendResponse({ result: result });
    }
  });
  