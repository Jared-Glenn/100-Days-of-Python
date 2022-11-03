import requests
from bs4 import BeautifulSoup
import smtplib
import security

SMTP_GMAIL = security.SMTP_GMAIL
gmail_email1 = security.gmail_email1
gmail_password1 = security.gmail_password1
gmail_email2 = security.gmail_email2
URL = "https://www.amazon.com/dp/B01H5QZ5X8"
desired_price = 119

headers = {
    "User-Agent": "Defined",
    "Accepted-Language": "en-US,en;q=0.5",
}

def check_price():
    response = requests.get(url=URL, headers=headers).text

    soup = BeautifulSoup(response, "html.parser")

    price = soup.find(name="span", class_="a-price-whole")

    if price == None:
        return None
    else:
        return price

running = True
counter = 0

while running:
    check = check_price()
    if counter >= 10:
        running = False
        print("Process Failed.")
    elif check == None:
        counter += 1
    else:
        price = check
        running = False


int_price = int(check.getText().strip("."))

if int_price <= desired_price:
    with smtplib.SMTP(SMTP_GMAIL) as connection:
        connection.starttls()
        connection.login(user=gmail_email1, password=gmail_password1)
        connection.sendmail(
            from_addr=gmail_email1,
            to_addrs=security.my_email,
            msg="Subject:Amazon-Bot: Foot Massager Price is Low!\n\nThe current price for the MIKO Foot Massager"
                f" is under ${desired_price + 1}."
        )



