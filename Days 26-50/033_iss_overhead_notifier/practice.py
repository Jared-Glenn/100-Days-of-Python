import requests
import datetime as dt

MY_LAT = 41.706120
MY_LON = -111.817848
LOCAL_UTC_OFFSET = -6

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    'formatted': 0,
}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
data = sun_response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

time_now = dt.datetime.now()
print(time_now)