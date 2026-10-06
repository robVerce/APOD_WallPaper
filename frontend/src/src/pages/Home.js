import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";
import { getApodPreview, setWallpaper } from '../api';

function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

const Home = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [apod, setApod] = useState(null);
  const [previewLoading, setPreviewLoading] = useState(false);
  const [previewError, setPreviewError] = useState(null);
  const [wallpaperStatus, setWallpaperStatus] = useState(null); // null | 'loading' | 'done' | 'error'
  const [wallpaperError, setWallpaperError] = useState(null);

  const handleGetImage = async () => {
    setPreviewLoading(true);
    setPreviewError(null);
    setApod(null);
    setWallpaperStatus(null);
    try {
      const result = await getApodPreview(formatDate(selectedDate));
      if (result.error) {
        setPreviewError(result.error);
      } else {
        setApod(result);
      }
    } catch (err) {
      setPreviewError(err.message);
    } finally {
      setPreviewLoading(false);
    }
  };

  const handleSetWallpaper = async () => {
    setWallpaperStatus('loading');
    setWallpaperError(null);
    try {
      const result = await setWallpaper(formatDate(selectedDate));
      if (result.error) {
        setWallpaperError(result.error);
        setWallpaperStatus('error');
      } else {
        setWallpaperStatus('done');
      }
    } catch (err) {
      setWallpaperError(err.message);
      setWallpaperStatus('error');
    }
  };

  return (
    <div className="columns-container">
      <div className="left-column">
        <h2>Date Selector</h2>
        <DatePicker selected={selectedDate} onChange={setSelectedDate} maxDate={new Date()} />
        <p>Selected Date: {selectedDate.toDateString()}</p>
        <div>
          <button className="btn" onClick={handleGetImage} disabled={previewLoading}>
            {previewLoading ? 'Fetching...' : 'Get Image'}
          </button>
        </div>
        <div>
          <button className="btn" onClick={handleSetWallpaper} disabled={!apod || wallpaperStatus === 'loading'}>
            {wallpaperStatus === 'loading' ? 'Setting wallpaper...' : 'Set as Wallpaper'}
          </button>
        </div>
        {wallpaperStatus === 'done' && <p>Wallpaper set!</p>}
        {wallpaperStatus === 'error' && <p className="settings-error">{wallpaperError}</p>}
      </div>

      <div className="right-column">
        {previewError && <p className="settings-error">{previewError}</p>}
        {apod && (
          <div>
            <h2>{apod.title}</h2>
            {apod.copyright && <p><em>{apod.copyright}</em></p>}
            <img src={apod.preview_url} alt={apod.title} style={{ maxWidth: '300px' }} />
            <p>{apod.explanation}</p>
          </div>
        )}
        {!apod && !previewLoading && !previewError && <p>Select a date and click "Get Image".</p>}
      </div>
    </div>
  );
};

export default Home;
