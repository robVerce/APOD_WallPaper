function waitForPywebview() {
  return new Promise((resolve) => {
    if (window.pywebview) {
      resolve();
      return;
    }
    window.addEventListener('pywebviewready', () => resolve(), { once: true });
  });
}

async function callApi(method, ...args) {
  await waitForPywebview();
  return window.pywebview.api[method](...args);
}

export function hasSettings() {
  return callApi('has_settings');
}

export function getSettings() {
  return callApi('get_settings');
}

export function saveSettings(pathSave) {
  return callApi('save_settings', pathSave);
}

export function getApod(date) {
  return callApi('get_apod', date);
}
