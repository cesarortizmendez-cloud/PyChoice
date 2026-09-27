/* pwa-install.js - Instalacion de PyChoice como app (Android, Windows, iPhone) */
(function () {
  var card = document.getElementById('install-card');
  var btn = document.getElementById('pwa-install-btn');
  var closeBtn = document.getElementById('pwa-install-close');
  var iosHelp = document.getElementById('pwa-ios-help');
  var deferred = null;

  // Registra el service worker
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('/service-worker.js').catch(function () {});
    });
  }

  var dismissed = false;
  try { dismissed = localStorage.getItem('pychoice.pwa.dismissed') === '1'; } catch (e) {}

  var isStandalone = window.matchMedia('(display-mode: standalone)').matches ||
    window.navigator.standalone === true;

  // Android / Chrome / Edge: evento nativo de instalacion
  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault();
    deferred = e;
    if (!dismissed && !isStandalone && card) { card.hidden = false; }
  });

  if (btn) btn.addEventListener('click', function () {
    if (!deferred) return;
    deferred.prompt();
    deferred.userChoice.finally(function () {
      deferred = null;
      if (card) card.hidden = true;
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', function () {
    if (card) card.hidden = true;
    try { localStorage.setItem('pychoice.pwa.dismissed', '1'); } catch (e) {}
  });

  // iOS: no hay evento; mostramos la guia manual
  var isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent);
  if (isIOS && !isStandalone && !dismissed && card && iosHelp) {
    card.hidden = false;
    if (btn) btn.style.display = 'none';
    iosHelp.hidden = false;
  }
})();
