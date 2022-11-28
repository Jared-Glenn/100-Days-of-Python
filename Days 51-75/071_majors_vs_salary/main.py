from bs4 import BeautifulSoup
import requests
import random
import pandas as pd

response = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
jobs_list = response.text

soup = BeautifulSoup(jobs_list, "html.parser")

data_list = []


rows = soup.find_all(name="tr", class_="data-table__row")

for row in rows:
    row_list = []
    cells = row.find_all(name="td", class_="data-table__cell")
    for cell in cells:
        data = cell.find_all('span')[1].getText()
        row_list.append(data)
    data_list.append(row_list)

cleaned_list = []

for row in data_list:
    row_list = []
    three = row[3].strip("$").replace(",", "")
    four = row[4].strip("$").replace(",", "")
    row_list.append(row[1])
    row_list.append(three)
    row_list.append(four)
    cleaned_list.append(row_list)

df = pd.DataFrame(cleaned_list)
df.columns = ["Major", "Early Career Pay", "Mid-Career Pay"]
df.to_csv("degrees_2021", index=False)


