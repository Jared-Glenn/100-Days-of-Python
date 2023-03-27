from bs4 import BeautifulSoup
import requests
import time

# locate top rated games that are at matching lows
# see about getting top reviews for each of these games

# search address: https://steamdb.info/sales/?min_reviews=100&min_rating=95&min_discount=0

site = "https://www.audible.com/search?creativeId=9648f6bf-4f29-4fb4-9489-33163c0bb63e&creativeId=9648f6bf-4f29-4fb4-9489-33163c0bb63e&creativeId=9648f6bf-4f29-4fb4-9489-33163c0bb63e&creativeId=9648f6bf-4f29-4fb4-9489-33163c0bb63e&feature_seven_browse-bin=18685633011&keywords=book&node=18580628011&pageLoadId=gcEEkgzwcLjacZkg&pageLoadId=Q6ROfiWTssPzMFv1&pageLoadId=SOa7pAbMYNmzYWgO&pageLoadId=Q7z6dlfobA00hxhX&publication_date=18685638011&ref=a_search_l1_feature_seven_browse-bin_3&pf_rd_p=daf0f1c8-2865-4989-87fb-15115ba5a6d2&pf_rd_r=55JCAYB0RQMN9WC9ZTZ2&pageLoadId=kQtjdB96bzEHRoEF&creativeId=9648f6bf-4f29-4fb4-9489-33163c0bb63e"


BROWSER_HEADER = {
        "Accept-Language": "en-US",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }

response = requests.get(url=site, headers=BROWSER_HEADER)
if '404' in response.url:
    raise Exception('No data found for this link.')

# This will not print on its own without '.encode(utf-8)' but bs4 needs to parse it without the encode.
soup = BeautifulSoup(response.content, "html.parser")


print(soup.div.text)


# title = soup.find("span", attrs={"class": "bc-text navigation-do-underline-on-hover"})

# print(title)

# title_value = title.string

# title_string = title_value.strip()

# print(title_string)



# spoonful = soup.find_all('div', attrs={"id": "product-list-a11y-skiplink-target"})

# table = spoonful.find_all('ul', attrs={"class": "bc-list"})

# for i in spoonful:
#     print(i.text)
#     print('\n')

# grid = soup.select_one["div{class=bc-col-responsive}"]
# listings = grid.find_all("tr")
# listing_list = []

# print(grid)

# /html/body/div[1]/div[5]/div[5]/div/div[2]


# for listing in listings:
#     if listing.select_one("a"):
#         address = listing.select_one("a").text
#         if listing.select_one("a").text == "Chevron Left":
#             break
#     else:
#         address = "N/A"
#     if listing.select_one("span"):
#         price_start = listing.select_one("span").text
#         price = price_start.split("+")[0]
#     else:
#         price = "N/A"
#     if listing.select_one("a"):
#         link = listing.select_one("a").get("href")
#         link = "https://www.zillow.com/" + link
#     else:
#         link = "N/A"
#     if address == "N/A" and price == "N/A" and link == "N/A":
#         continue
#     listing_list.append({
#         "address": address,
#         "price": price,
#         "link": link,
#     })

