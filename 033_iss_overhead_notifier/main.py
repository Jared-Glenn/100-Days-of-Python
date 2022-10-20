import time

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


import requests
import datetime as dt
import smtplib
import acct_info


def isCloseEnough(iss_lat, iss_lon):
    if (iss_lat > MY_LAT - 5 and iss_lat < MY_LAT + 5 and iss_lon > MY_LON - 5 and iss_lon< MY_LON + 5):
        return True
    else:
        return False


def isDarkOut(sunrise, sunset):
    time_now = dt.datetime.now()
    print(time_now)

    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


MY_LAT = 41.706120
MY_LON = -111.817848
LOCAL_UTC_OFFSET = -6
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    'formatted': 0,
}


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
latitude = float(response.json()["iss_position"]["latitude"])
longitude = float(response.json()["iss_position"]["longitude"])


sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
data = sun_response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


while True:
    time.sleep(60)
    if isCloseEnough(latitude, longitude) and isDarkOut(sunshine, sunset):
        with smtplib.SMTP(acct_info.SMTP_GMAIL) as connection:
            connection.starttls()
            connection.login(user=acct_info.gmail_email1, password=acct_info.gmail_password1)
            connection.sendmail(
                from_addr=acct_info.gmail_email1,
                to_addrs=acct_info.gmail_email2,
                msg="Subject:Look Up!☝\n\nThe International Space Station is Overhead in Providence, "
                    "Utah, and its dark enough that you can see it!\n\nTake a look!\n\n-Jared"
            )


