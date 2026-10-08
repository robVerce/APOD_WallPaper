import React, { useEffect, useState } from 'react';
import { getSettings, saveSettings, isAutoUpdateEnabled, enableAutoUpdate, disableAutoUpdate } from '../api';

const Settings = ({ onSaved }) => {
  const [settings, setSettings] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);

  const [autoUpdate, setAutoUpdate] = useState(null);
  const [autoUpdateBusy, setAutoUpdateBusy] = useState(false);
  const [autoUpdateError, setAutoUpdateError] = useState(null);

  useEffect(() => {
    getSettings()
      .then(setSettings)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));

    isAutoUpdateEnabled()
      .then(setAutoUpdate)
      .catch((err) => setAutoUpdateError(err.message));
  }, []);

  const handleChooseFolder = async () => {
    setSaving(true);
    setError(null);
    try {
      const newSettings = await saveSettings();
      setSettings(newSettings);
      if (onSaved) onSaved(newSettings);
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  const handleToggleAutoUpdate = async () => {
    setAutoUpdateBusy(true);
    setAutoUpdateError(null);
    try {
      const result = autoUpdate ? await disableAutoUpdate() : await enableAutoUpdate();
      if (result.error) {
        setAutoUpdateError(result.error);
      } else {
        setAutoUpdate(result.enabled);
      }
    } catch (err) {
      setAutoUpdateError(err.message);
    } finally {
      setAutoUpdateBusy(false);
    }
  };

  if (loading) {
    return <p>Loading settings...</p>;
  }

  return (
    <div className="settings-page">
      <h2>Settings</h2>

      {settings && (
        <div className="settings-summary">
          <p><strong>Save folder:</strong> {settings.path_save}</p>
          <p><strong>Screen resolution:</strong> {settings.screen_width} x {settings.screen_height}</p>
        </div>
      )}

      <button className="btn" onClick={handleChooseFolder} disabled={saving}>
        {saving ? 'Waiting for folder selection...' : 'Choose save folder'}
      </button>

      {error && <p className="settings-error">{error}</p>}

      <div className="settings-auto-update">
        <h3>Automatic Daily Update</h3>
        <p>
          {autoUpdate === null
            ? 'Checking status...'
            : autoUpdate
              ? 'Enabled — the wallpaper updates automatically every day at 8:00 AM.'
              : 'Disabled.'}
        </p>
        <button
          className="btn"
          onClick={handleToggleAutoUpdate}
          disabled={autoUpdate === null || autoUpdateBusy}
        >
          {autoUpdateBusy
            ? 'Updating...'
            : autoUpdate
              ? 'Disable automatic updates'
              : 'Enable automatic updates'}
        </button>
        {autoUpdateError && <p className="settings-error">{autoUpdateError}</p>}
      </div>
    </div>
  );
};

export default Settings;
