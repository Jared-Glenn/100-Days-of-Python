##################### Extra Hard Starting Project ######################
import smtplib
import acct_info
from random import choice
import datetime as dt
import pandas

now = dt.datetime.now()
now_month = now.month
now_day = now.day

birthdays = pandas.read_csv('birthdays.csv')

for index in range(len(birthdays) - 1):
    if birthdays["day"][index] == now_day and birthdays["month"][index] == now_month:
        letter_text = choice(["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"])
        name = birthdays["name"][index]
        with open(letter_text, "r") as letter_data:
            letter_lines = letter_data.readlines()
            letter = ""
            for line in letter_lines:
                letter += line
            letter = letter.replace("[NAME]", name)
        with smtplib.SMTP(acct_info.SMTP_GMAIL) as connection:
            connection.starttls()
            connection.login(user=acct_info.gmail_email1, password=acct_info.gmail_password1)
            connection.sendmail(
                from_addr=acct_info.gmail_email1,
                to_addrs=birthdays["email"][index],
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )
