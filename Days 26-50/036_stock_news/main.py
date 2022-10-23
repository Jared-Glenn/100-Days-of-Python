import os
import requests
import datetime as dt
from datetime import date, timedelta
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "R37YZRVNNX0H1BX0"
NEWS_API_KEY = "fd9a07900ed3483eb567ac30c5717a61"


def write_news(stock_symbol, news_data):
    news_return ='''
       \n--- {0} ---
       {1}
       "{2}"
       {3}

       {4}
       "{5}"
       {6}

       {7}
       "{8}"
       {9}
       '''.format(stock_symbol, news_data["articles"][0]["source"]["name"], news_data["articles"][0]["title"],
                  news_data["articles"][0]["url"],
                  news_data["articles"][1]["source"]["name"], news_data["articles"][1]["title"],
                  news_data["articles"][1]["url"],
                  news_data["articles"][2]["source"]["name"], news_data["articles"][2]["title"],
                  news_data["articles"][2]["url"], )

    return news_return



now = dt.datetime.now()
today = f"{now.year}-{now.month}-{now.day}"

if now.weekday == 0:
    yest = date.today() - timedelta(days=3)
    yesterday = f"{yest.year}-{yest.month}-{yest.day}"
else:
    yest = date.today() - timedelta(days=1)
    yesterday = f"{yest.year}-{yest.month}-{yest.day}"


stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY,
}

news_parameters = {
    "q" : COMPANY_NAME,
    "from" : today,
    "sortBy" : "publishedAt",
    "language" : "en",
    "apiKey" : NEWS_API_KEY
}


stock_report = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_report.raise_for_status()
stock_data = stock_report.json()

today_price = float(stock_data["Time Series (Daily)"][today]["1. open"])
yest_price = float(stock_data["Time Series (Daily)"][yesterday]["1. open"])
cut_off = yest_price * 0.05
diff = yest_price - today_price
difference = abs(diff)
dif_percent = abs((difference/yest_price)*100)
if diff > 0:
    stock_symbol = f"TSLA 🔺{dif_percent}%"
else:
    stock_symbol = f"TSLA 🔻{dif_percent}%"


if difference >= cut_off:
    news_report = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_report.raise_for_status()
    news_data = news_report.json()

    news_return = write_news(stock_symbol, news_data)

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(twilio_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body=news_return,
        from_="+15618234125",
        to="+14355123350"
    )

