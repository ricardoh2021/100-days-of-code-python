import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

class Spotify:
    load_dotenv()  # Load environment variables from .env file

    def __init__(self):
        # Use SpotifyOAuth for user-based authentication
        scope = "playlist-modify-public playlist-modify-private"

        auth_manager = SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri="https://www.google.com/",
            scope=scope  # This scope allows access to the current user's profile
        )

        self.sp = spotipy.Spotify(auth_manager=auth_manager)

        # Fetch and print the current user's profile information
        self.user = self.sp.current_user()
        # print(self.user)

    def get_user_id(self) -> str:
        return str(self.user["id"])

    def search_song_uri(self, track_name, year):
        # Use the query format "track: {name} year: {YYYY}"
        query = f"track: {track_name} year: {year}"
        result = self.sp.search(q=query, type='track', limit=1)

        if result['tracks']['items']:
            # Return the URI of the first matching track
            return result['tracks']['items'][0]['uri']
        else:
            # No match found
            return None

    def create_playlist(self, user, date):
        new_playlist = self.sp.user_playlist_create(user=user, name=f"{date} Billboard Top 100")
        id = new_playlist["id"]
        return id

    def add_to_playlist(self, playlist_id, song_uris):
        self.sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

# Instantiate the class to trigger the authentication and fetch the user data
# spotify_client = Spotify()