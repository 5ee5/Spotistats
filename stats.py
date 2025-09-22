import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
import json
from dotenv import load_dotenv

# ----------- LOAD ENV VARIABLES -----------
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

SCOPE = "user-top-read user-read-recently-played"

# ----------- AUTHENTICATION -----------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=".cache",
    show_dialog=False
))

# ----------- SAVE JSON (overwrite) -----------
def save_json(df, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=2)

# ----------- FETCH TOP ARTISTS -----------
def get_top_artists(limit=10, time_range="long_term"):
    results = sp.current_user_top_artists(limit=limit, time_range=time_range)
    df = pd.DataFrame([{
        "name": a["name"],
        "popularity": a["popularity"],
        "genres": ", ".join(a["genres"])
    } for a in results["items"]])
    return df

# ----------- FETCH TOP TRACKS -----------
def get_top_tracks(limit=10, time_range="long_term"):
    results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    df = pd.DataFrame([{
        "name": t["name"],
        "artist": t["artists"][0]["name"],
        "popularity": t["popularity"]
    } for t in results["items"]])
    return df

# ----------- FETCH RECENTLY PLAYED -----------
def get_recently_played(limit=20):
    results = sp.current_user_recently_played(limit=limit)
    df = pd.DataFrame([{
        "played_at": t["played_at"],
        "name": t["track"]["name"],
        "artist": t["track"]["artists"][0]["name"],
        "album": t["track"]["album"]["name"]
    } for t in results["items"]])
    return df

# ----------- MAIN FETCHER -----------
def fetch_all_data(limit=10):
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(base_dir, exist_ok=True)

    time_ranges = {
        "short_term": "4_weeks",
        "medium_term": "6_months",
        "long_term": "lifetime"
    }

    # Save top artists + tracks per time range
    for tr, folder in time_ranges.items():
        out_dir = os.path.join(base_dir, folder)
        os.makedirs(out_dir, exist_ok=True)

        artists_df = get_top_artists(limit=limit, time_range=tr)
        save_json(artists_df, os.path.join(out_dir, "artists.json"))

        tracks_df = get_top_tracks(limit=limit, time_range=tr)
        save_json(tracks_df, os.path.join(out_dir, "tracks.json"))

    # Save recently played directly in root folder
    recent_df = get_recently_played(limit=50)
    save_json(recent_df, os.path.join(base_dir, "recently_played.json"))

# ----------- RUN -----------
if __name__ == "__main__":
    fetch_all_data(limit=20)

