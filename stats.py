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

SCOPE = "user-top-read"

# ----------- AUTHENTICATION -----------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=".cache",
    show_dialog=False
))

# ----------- HELPER TO SAVE JSON APPENDING NEW ROWS -----------
def save_json_append(df, filename):
    existing = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            existing = json.load(f)
    existing.extend(df.to_dict(orient="records"))
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

# ----------- FETCH TOP ARTISTS -----------
def get_top_artists(limit=10, time_range='medium_term'):
    results = sp.current_user_top_artists(limit=limit, time_range=time_range)
    df = pd.DataFrame([{
        'name': a['name'],
        'popularity': a['popularity'],
        'genres': ', '.join(a['genres'])
    } for a in results['items']])
    save_json_append(df, "top_artists.json")
    return df

# ----------- FETCH TOP TRACKS -----------
def get_top_tracks(limit=10, time_range='medium_term'):
    results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    df = pd.DataFrame([{
        'name': t['name'],
        'artist': t['artists'][0]['name'],
        'popularity': t['popularity']
    } for t in results['items']])
    save_json_append(df, "top_tracks.json")
    return df

# ----------- MAIN -----------
if __name__ == "__main__":
    get_top_artists()
    get_top_tracks()

