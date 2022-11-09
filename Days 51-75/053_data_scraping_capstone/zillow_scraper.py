from bs4 import BeautifulSoup
import requests

class ZillowScraper():
    def __init__(self):
        self.site = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7" \
                    "D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.77085581867854%2C%22east%22%3A-122.14944" \
                    "163410823%2C%22south%22%3A37.611066454992844%2C%22north%22%3A37.92154937638743%7D%2C" \
                    "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%" \
                    "7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%" \
                    "22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22" \
                    "value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%" \
                    "3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse" \
                    "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
        self.listings = []

    def get_data(self):
        BROWSER_HEADER = {
            "Accept-Language": "en-US",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
        }

        response = requests.get(url=self.site, headers=BROWSER_HEADER)
        if '404' in response.url:
            raise Exception('No data found for this link.')
        data = response.text

        soup = BeautifulSoup(data, "html.parser")

        grid = soup.select_one("div[id=search-page-list-container]")
        listings = grid.find_all("li")

        listing_list = []
        for listing in listings:
            if listing.select_one("a"):
                address = listing.select_one("a").text
                if listing.select_one("a").text == "Chevron Left":
                    break
            else:
                address = "N/A"

            if listing.select_one("span"):
                price_start = listing.select_one("span").text
                price = price_start.split("+")[0]
            else:
                price = "N/A"

            if listing.select_one("a"):
                link = listing.select_one("a").get("href")
                link = "https://www.zillow.com/" + link
            else:
                link = "N/A"

            if address == "N/A" and price == "N/A" and link == "N/A":
                continue

            listing_list.append({
                "address": address,
                "price": price,
                "link": link,
            })

        self.listings = listing_list
        return self.listings
