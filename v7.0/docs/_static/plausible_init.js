// Plausible analytics initialisation shim.
// Pairs with the async script loaded via html_js_files in _config.yml.
window.plausible = window.plausible || function () {
  (plausible.q = plausible.q || []).push(arguments);
};
plausible.init = plausible.init || function (i) {
  plausible.o = i || {};
};
plausible.init();
