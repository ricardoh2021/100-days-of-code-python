import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

contents = res.text

soup = BeautifulSoup(contents, "html.parser")

movie_titles = []

movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")


with open("movie_ranking.txt", mode="w") as file:
    for movie in reversed(movie_titles):
        file.write(f"{movie.getText()}\n")