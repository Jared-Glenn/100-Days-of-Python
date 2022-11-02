from bs4 import BeautifulSoup
import requests


class WebScraper:
    def __init__(self):
        self.date = input("FLUX CAPACITOR: INPUT DATE YYYY-MM-DD")
        self.site = f"https://www.billboard.com/charts/hot-100/{self.date}/"
        self.song_list = []

    def get_date(self):
        self.date = input("FLUX CAPACITOR: INPUT DATE YYYY-MM-DD")
        self.site = f"https://www.billboard.com/charts/hot-100/{self.date}/"

    def get_songs(self):
        response = requests.get(self.site)
        data = response.text

        soup = BeautifulSoup(data, "html.parser")

        first_level = soup.find_all(name="div", class_="o-chart-results-list-row-container")

        for place in first_level:
            second_level = place.find(name="li", class_="lrv-u-width-100p")
            title = second_level.find(name="h3", id="title-of-a-story")
            artist = second_level.find(name="span", class_="c-label")
            artist = artist.getText().strip().split()[0]
            new_song = [title.getText().strip(), artist]
            self.song_list.append(new_song)
        return self.song_list