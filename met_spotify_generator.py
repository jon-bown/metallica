import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import datetime
from kaggle.api.kaggle_api_extended import KaggleApi
import utils.update_metadata as update_metadata

# GET SECRETS
SPOTIFY_ID = os.getenv('SPOTIFY_ID')
SPOTIFY_KEY = os.getenv('SPOTIFY_KEY')

#Spotify Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_KEY)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#initialize dataframes
met_data = []

#Get UNIQUE ALBUMS
met_uri = 'spotify:artist:2ye2Wgw4gimLv2eAKyk1NB'

results = sp.artist_albums(met_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

names = []
album_ids = []
for album in albums:
    name = album['name'].lower()
    if name not in names:
        names.append(name)
        album_ids.append(album['id'])


#Construct track specific data
for album_id in album_ids:
    results = sp.album_tracks(album_id)
    album_info = sp.album(album_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    track_ids = []
    for track in tracks:
        track_row = {}
        track_row['spotify_id'] = track['id']
        track_row['spotify_uri'] = track['uri']
        track_row['album'] = album_info['name']
        track_row['name'] = track['name']
        track_row['release_date'] = album_info['release_date']
        track_row['track_number'] = track['track_number']
        try:
            popularity = sp.track(track['id'])['popularity']
            track_row['popularity'] = popularity
        except:
            popularity = float('nan')
        track_ids.append(track['id'])
        features = sp.audio_features(track['id'])[0]
        track_row['danceability'] = features['danceability']
        track_row['energy'] = features['energy']
        track_row['key'] = features['key']
        track_row['loudness'] = features['loudness']
        track_row['mode'] = features['mode']
        track_row['speechiness'] = features['speechiness']
        track_row['acousticness'] = features['acousticness']
        track_row['instrumentalness'] = features['instrumentalness']
        track_row['liveness'] = features['liveness']
        track_row['valence'] = features['valence']
        track_row['tempo'] = features['tempo']
        track_row['duration_ms'] = features['duration_ms']
        track_row['time_signature'] = features['time_signature']
        met_data.append(track_row)

#Convert result to pandas
cols = ['spotify_id', 'spotify_uri', 'album', 'name', 'popularity', 'release_date', 'track_number', 'danceability', 'energy',
       'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms', 'time_signature']
metallica_data = pd.DataFrame(met_data, columns = cols)        



#Check if new data added
prev_song_data = pd.read_csv('./song-data/metallica_songs.csv')

SAME = prev_song_data.shape == metallica_data.shape

#if not the same, update
if not SAME:
    metallica_data.to_csv('./song-data/metallica_songs.csv', index=False)
    update_metadata.update_description()
    api = KaggleApi()
    api.authenticate()

    api.dataset_create_version(
    "./song-data/",
    version_notes=f"Updated on {datetime.datetime.now().strftime('%Y-%m-%d')}",
    )
