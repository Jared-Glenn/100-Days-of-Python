from bs4 import BeautifulSoup
import requests
import csv


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

book_lib = []

# Add book title to list
h3_list = soup.find_all("h3")
for h3 in h3_list:
    links = h3.find_all("a")
    if links:
        for link in links:
            title = link.string
            book_lib.append([title])


# Create a price list
price_list = []
p_list = soup.find_all("p")
for p in p_list:
    spans = p.find_all("span")
    if spans:
        for span in spans:
            price = span.string.strip()
            if price.find("$") >= 0:
                price_list.append(price)

# Match prices to their books.
index = 0
for x, price in enumerate(price_list):
    if x%2 == 0:
        if book_lib[index]:
            book_lib[index].append(price)
            index += 1

# Find ratings information (Note the underscore after class due to 'class' being reserved)
index = 0
li_list = soup.find_all(class_="ratingsLabel")
for li in li_list:
    spans = li.find_all(class_="bc-text bc-pub-offscreen")
    for span in spans:
        stars = span.string.strip()
        book_lib[index].append(stars)
    spans = li.find_all(class_="bc-text bc-size-small bc-color-secondary")
    for span in spans:
        ratings = span.string.strip()
        book_lib[index].append(ratings)
    index += 1


# Move the list of lists into a CSV file.
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(book_lib)

