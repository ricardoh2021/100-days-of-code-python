from datetime import datetime
import requests
from bs4 import BeautifulSoup
from spotify import Spotify


def get_valid_date() -> str:
    """
    Continuously prompts the user for a date until a valid date is entered.
    :return: The validated date string in the format 'YYYY-MM-DD'
    """
    while True:
        date_input = input("Which year would you like to travel to? Please input text in YYYY-MM-DD format: ")

        try:
            # Attempt to parse the input string into a valid date
            valid_date = datetime.strptime(date_input, "%Y-%m-%d")
            print(f"Valid date entered: {valid_date.strftime('%Y-%m-%d')}")
            return valid_date.strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please try again with the correct format: YYYY-MM-DD.")


def scrape_billboard_top_100(date: str) -> list:
    """
    Scrapes the Billboard Hot 100 chart for the given date.
    :param date: Date in 'YYYY-MM-DD' format
    :return: List of song names from the Billboard chart
    """
    billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    res = requests.get(billboard_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    billboard_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

    song_list = []
    for song in billboard_songs:
        title_block = song.find(name="li", class_="lrv-u-width-100p")
        if title_block:
            h3 = title_block.find("h3")
            if h3:
                song_list.append(h3.getText().strip())
    return song_list


def main():
    # Get the valid date input from the user
    valid_date = get_valid_date()
    year = valid_date.split("-")[0]  # Extract the year

    # Scrape Billboard Top 100 songs for the entered date
    song_list = scrape_billboard_top_100(valid_date)
    print("Songs found on Billboard Hot 100:", song_list)

    # Initialize the Spotify API wrapper
    spotify_user = Spotify()

    # Search for Spotify URIs for each song
    spotify_uris = []
    for song in song_list:
        uri = spotify_user.search_song_uri(song, year)
        if uri:
            print(f"Found URI for {song}: {uri}")
            spotify_uris.append(uri)
        else:
            print(f"Song {song} not found on Spotify.")

    # Create a playlist and add the songs
    if spotify_uris:
        playlist_id = spotify_user.create_playlist(spotify_user.get_user_id(), valid_date)
        spotify_user.add_to_playlist(playlist_id, spotify_uris)
        print(f"Playlist created successfully with {len(spotify_uris)} songs.")
    else:
        print("No songs were found on Spotify to add to the playlist.")


if __name__ == "__main__":
    main()