// Impede que novas abas venham para frente automaticamente
chrome.tabs.onCreated.addListener((tab) => {
  if (tab.id) {
    // Mantém a aba atual ativa
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
      if (tabs[0] && tabs[0].id !== tab.id) {
        chrome.tabs.update(tabs[0].id, {active: true});
      }
    });
  }
});
