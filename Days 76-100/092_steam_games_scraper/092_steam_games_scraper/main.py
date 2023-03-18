from bs4 import BeautifulSoup
import requests

# locate top rated games that are at matching lows
# see about getting top reviews for each of these games

# search address: https://steamdb.info/sales/?min_reviews=100&min_rating=95&min_discount=0

site = "https://steamdb.info/sales/?min_reviews=100&min_rating=95&min_discount=0"

BROWSER_HEADER = {
        "Accept-Language": "en-US",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }

response = requests.get(url=site, headers=BROWSER_HEADER)
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

