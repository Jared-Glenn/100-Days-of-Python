import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



api_key = os.environ.get("OMW_API_KEY")
account_sid = "AC65fcc5a0563c1ed5cdd3abe264afbbdc"
auth_token = os.environ.get("AUTH_TOKEN")

MY_LAT = 41.706120
MY_LON = -111.817848

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

will_rain = False

for i in range(0, 25):
    weather_data = response.json()["hourly"][i]["weather"][0]["id"]
    if weather_data < 700:
        will_rain = True


if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+15618234125",
        to="+14355123350"
    )

    print(message.status)
