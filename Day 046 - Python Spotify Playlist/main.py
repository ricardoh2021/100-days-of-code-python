from datetime import datetime
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from spotify import Spotify


# Set up headers with a user-agent that mimics a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

while True:
    date_input = input("Which year would you like to travel to? Please input text in YYYY-MM-DD format: ")

    try:
        # Attempt to parse the input string into a valid date
        valid_date = datetime.strptime(date_input, "%Y-%m-%d")
        year = valid_date.year
        month = valid_date.month
        day = valid_date.day
        print(f"Valid date entered: {valid_date.strftime('%Y-%m-%d')}")
        break  # Exit the loop if the input is valid
    except ValueError:
        # If parsing fails, print an error message and ask for input again
        print("Invalid date format. Please try again with the correct format: YYYY-MM-DD.")

valid_date = valid_date.strftime('%Y-%m-%d')


billboard_url = f"https://www.billboard.com/charts/hot-100/{valid_date}"


res = requests.get(billboard_url, headers=headers)
contents = res.text

soup = BeautifulSoup(contents, "html.parser")

billboard_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
title_blocks = []

for song in billboard_songs:
    title_block = song.find(name="li", class_="lrv-u-width-100p")
    title_blocks.append(title_block)

song_list = []

for title in title_blocks:
    h3 = title.find("h3")
    song = h3.getText().strip()
    song_list.append(song)

print(song_list)

user = Spotify()

# url = input("Enter the URL you were redirected to: ")
#
# with open("token.txt", mode="w") as file:
#     file.write(url)

# List to store Spotify URIs
spotify_uris = []

for song in song_list:
    # Search for the song on Spotify
    uri = user.search_song_uri(song, year)

    if uri:
        print(f"Found URI for {song}: {uri}")
        spotify_uris.append(uri)
    else:
        print(f"Song {song} not found on Spotify.")

# The list `spotify_uris` now contains the URIs for the songs
print(spotify_uris)

playlist_id = user.create_playlist(user=user.get_user_id(), date=valid_date)

user.add_to_playlist(playlist_id=playlist_id, song_uris=spotify_uris)

