# Spotistats

A simple Python script to fetch your **Spotify top artists and tracks** and save them to JSON files for analysis or backup.

---

## Features

- Fetch top artists and tracks in 3 timeframes (4weeks, 6months, lifetime) using Spotify Web API
- Save results to JSON files (`top_artists.json`, `top_tracks.json`) and saves them into corresponding time frame direcotry (`last 4 weeks`, `last 6 months`, `lifetime`).
- also saves recently played tracks into (`recently_played.json`)
- Clean JSON output (overwrites on each run, no duplicate entries)
- Uses `.env` file for credentials to keep them secure
- Fully silent; no data is printed by default

---

### Setup
#### Install dependencies with:

```bash
pip install -r requirements.txt
```
---

#### Add you credentials:
```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

