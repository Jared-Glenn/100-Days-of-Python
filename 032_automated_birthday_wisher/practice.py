# import smtplib
# import acct_info
#
# my_email = acct_info.gmail_email1
# password = acct_info.gmail_password1
#
# with smtplib.SMTP(acct_info.SMTP_GMAIL) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=acct_info.gmail_email2,
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=1985, month=9, day=24)
#
# print(date_of_birth)



