import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

class Spotify:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        # Set the scope for creating and modifying playlists
        scope = "playlist-modify-public playlist-modify-private"

        # Initialize SpotifyOAuth for user authentication
        auth_manager = SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI", "https://www.google.com/"),
            scope=scope
        )

        self.sp = spotipy.Spotify(auth_manager=auth_manager)
        self.user = self.sp.current_user()

    def get_user_id(self) -> str:
        """
        Returns the Spotify user ID of the authenticated user.
        """
        return str(self.user["id"])

    def search_song_uri(self, track_name: str, year: str) -> str:
        """
        Searches Spotify for a track by name and year.
        :param track_name: The name of the track to search for.
        :param year: The year the track was released.
        :return: The URI of the track if found, otherwise None.
        """
        query = f"track: {track_name} year: {year}"
        result = self.sp.search(q=query, type='track', limit=1)

        if result['tracks']['items']:
            return result['tracks']['items'][0]['uri']
        return None

    def create_playlist(self, user_id: str, date: str) -> str:
        """
        Creates a Spotify playlist for the authenticated user.
        :param user_id: The user ID of the Spotify account.
        :param date: The date to use in the playlist title.
        :return: The ID of the created playlist.
        """
        playlist_name = f"{date} Billboard Top 100"
        new_playlist = self.sp.user_playlist_create(user=user_id, name=playlist_name)
        return new_playlist["id"]

    def add_to_playlist(self, playlist_id: str, song_uris: list):
        """
        Adds a list of song URIs to a Spotify playlist.
        :param playlist_id: The ID of the Spotify playlist.
        :param song_uris: A list of Spotify track URIs to add to the playlist.
        """
        self.sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)