import React, { useEffect, useState } from 'react';
import { getSettings, saveSettings } from '../api';

const Settings = ({ onSaved }) => {
  const [settings, setSettings] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    getSettings()
      .then(setSettings)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
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

  if (loading) {
    return <p>Loading settings...</p>;
  }

  return (
    <div className="settings-page">
      <h2>Settings</h2>

      {settings ? (
        <div className="settings-summary">
          <p><strong>Save folder:</strong> {settings.path_save}</p>
          <p><strong>Screen resolution:</strong> {settings.screen_width} x {settings.screen_height}</p>
        </div>
      ) : (
        <p>No save folder configured yet. Choose one to get started.</p>
      )}

      <button onClick={handleChooseFolder} disabled={saving}>
        {saving ? 'Waiting for folder selection...' : 'Choose save folder'}
      </button>

      {error && <p className="settings-error">{error}</p>}
    </div>
  );
};

export default Settings;
