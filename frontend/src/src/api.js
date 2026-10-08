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

export function getSettings() {
  return callApi('get_settings');
}

export function saveSettings(pathSave) {
  return callApi('save_settings', pathSave);
}

export function getApodPreview(date) {
  return callApi('get_apod_preview', date);
}

export function setWallpaper(date) {
  return callApi('set_wallpaper', date);
}

export function isAutoUpdateEnabled() {
  return callApi('is_auto_update_enabled');
}

export function enableAutoUpdate() {
  return callApi('enable_auto_update');
}

export function disableAutoUpdate() {
  return callApi('disable_auto_update');
}
