# Spotistats

A simple Python script to fetch your **Spotify top artists and tracks** and save them to JSON files for analysis or backup.

---

## Features

- Fetch top artists and tracks in 3 timeframes (4weeks, 6months, lifetime) using Spotify Web API
- Save results to JSON files (`artists.json`, `tracks.json`) and saves them into corresponding time frame directory (`4 weeks`, `6 months`, `lifetime`).
- Also saves recently played tracks into (`recently_played.json`)
- Clean JSON output (overwrites on each run, no duplicate entries)
- Uses `.env` file for credentials to keep them secure
- Fully silent; no data is printed by default

---

### Setup

#### Setup / API Credentials

This project uses the Spotify Web API. To use it, you need your own Spotify credentials:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click **"Create an App"** and fill in the details.
4. After creating the app, copy the **Client ID** and **Client Secret**.
5. Set a **Redirect URI**, for example: `http://localhost:8888/callback`.


#### Install dependencies with:

```bash
pip install -r requirements.txt
```

#### Add your credentials into the .env file:
```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_url
```

