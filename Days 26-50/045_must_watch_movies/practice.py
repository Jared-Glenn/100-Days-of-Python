from bs4 import BeautifulSoup
import requests
import numpy


# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # .findall()
# # .getText()
# # .get()
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# heading = soup.select(".heading")
# print(heading)

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(".titleline")
article_titles = []
article_links = []
for article_tag in articles:
    article_tag = article_tag.select_one("a")
    title = article_tag.getText()
    article_titles.append(title)
    link = article_tag.get("href")
    article_links.append(link)


article_scores = [int(score.getText().split()[0]) for score in soup.select(".score")]

print(article_titles)
print(article_links)
print(article_scores)

max_value = numpy.argmax(article_scores)

print(article_titles[max_value], article_links[max_value])

