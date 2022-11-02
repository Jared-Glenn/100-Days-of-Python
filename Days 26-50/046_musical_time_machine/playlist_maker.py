import spotipy
from spotipy.oauth2 import SpotifyOAuth
import security

SPOTIFY_CLIENT_ID = security.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = security.SPOTIFY_CLIENT_SECRET


class PlaylistMaker:
    def __init__(self, song_list):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                            client_secret=SPOTIFY_CLIENT_SECRET,
                                                            redirect_uri="http://example.com",
                                                            scope="user-library-read playlist-modify-public"))
        self.user_id = self.sp.current_user()["id"]
        self.song_list = song_list
        self.playlist_id = None
        self.id_list = []

    def create_playlist(self, date):
        playlist = self.sp.user_playlist_create(self.user_id, f"Billboard's Top 100 on {date}", public=True, collaborative=False,
                             description=f'Musical Time Machine to {date}')
        self.playlist_id = playlist["id"]

    def search_songs(self):
        for song in self.song_list:
            try:
                results = self.sp.search(q=f"track:{song[0]} artist:{song[1]}", type="track")
                self.id_list.append(results["tracks"]["items"][0]["id"])
            except:
                results = self.sp.search(q=f"track:{song[0]}", type="track")
                self.id_list.append(results["tracks"]["items"][0]["id"])

    def add_songs(self):
        self.sp.playlist_add_items(self.playlist_id, self.id_list)

