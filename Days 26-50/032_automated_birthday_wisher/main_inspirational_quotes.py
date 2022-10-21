import smtplib
import acct_info
import datetime as dt
from random import randint

my_email = acct_info.gmail_email1
password = acct_info.gmail_password1

with open("quotes.txt", "r") as data:
    quotes = data.readlines()

quote = quotes[randint(0, (len(quotes) - 1))]

now = dt.datetime.now()
if now.weekday() == 2:
    with smtplib.SMTP(acct_info.SMTP_GMAIL) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=acct_info.gmail_email2,
            msg=f"Subject:Inspirational Quote Time!\n\n{quote}"
        )