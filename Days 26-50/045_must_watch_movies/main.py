from bs4 import BeautifulSoup
import requests
import random

def pick_movie(title_list):
    movie_choice = random.choice(title_list)
    print(f"Next, let's have you watch {movie_choice}")

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_list = response.text

soup = BeautifulSoup(movie_list, "html.parser")

titles = soup.find_all(name="img", class_="jsx-952983560 loading")

title_list = []
for title in titles:
    text = title.get("alt")
    title_list.append(text)

title_list = title_list[1:]
title_list.reverse()

pick_movie(title_list)

with open("movies.txt", mode="w") as file:
    for i, movie in enumerate(title_list):
        file.write(f"{i+1}) {movie}\n")


# .jsx-4245974604

