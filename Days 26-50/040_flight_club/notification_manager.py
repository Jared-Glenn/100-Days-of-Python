from twilio.rest import Client
import smtplib
import security

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.api_key = security.TWILIO_API_KEY
        self.auth_token = security.TWILIO_AUTH_TOKEN
        self.acct_sid = security.TWILIO_ACCT_SID

    def send_message(self, deal_list):
        for deal in deal_list:
            link = deal['deep_link']
            # link = f"https://www.google.co.uk/flights?hl=en#flt={deal['dep_aita_code']}" \
            #        f".{deal['arr_aita_code']}.{deal['out_date']}*{deal['arr_aita_code']}" \
            #        f".{deal['dep_aita_code']}.{deal['in_date']}"

            low_price_alert = f"Low price alert! Only £{deal['price']} to fly from " \
                              f"{deal['dep_city']}-{deal['dep_aita_code']} to " \
                              f"{deal['arr_city']}-{deal['arr_aita_code']}, from " \
                              f"{deal['out_date']} to {deal['in_date']}."

            if deal["stop_overs"] == 2:
                low_price_alert += "\n\n"
                low_price_alert += f" Flight has 1 stop over via {deal['via_city']}."

            low_price_alert += "\n\n"
            low_price_alert += f"{link}"

            client = Client(self.acct_sid, self.auth_token)

            message = client.messages \
                .create(
                    body=low_price_alert,
                    from_="+15618234125",
                    to="+14355123350"
                )
            print(message.status)

    def send_emails(self, deal_list, email_list):
        email_message = ""

        for deal in deal_list:
            link = deal['deep_link']
            # link = f"https://www.google.co.uk/flights?hl=en#flt={deal['dep_aita_code']}" \
            #        f".{deal['arr_aita_code']}.{deal['out_date']}*{deal['arr_aita_code']}" \
            #        f".{deal['dep_aita_code']}.{deal['in_date']}"

            low_price_alert = f"Low price alert! Only £{deal['price']} to fly from " \
                              f"{deal['dep_city']}-{deal['dep_aita_code']} to " \
                              f"{deal['arr_city']}-{deal['arr_aita_code']}, from " \
                              f"{deal['out_date']} to {deal['in_date']}."

            if deal["stop_overs"] == 2:
                low_price_alert += "\n\n"
                low_price_alert += f" Flight has 1 stop over via {deal['via_city']}."

            low_price_alert += "\n\n"
            low_price_alert += f"{link}"

            email_message += low_price_alert
            email_message += "\n\n\n"

        for email in email_list:
            with smtplib.SMTP(security.SMTP_GMAIL) as connection:
                connection.starttls()
                connection.login(user=security.gmail_email1, password=security.gmail_password1)
                connection.sendmail(
                    from_addr= security.gmail_email1,
                    to_addrs= email['email'],
                    msg= f"Subject:New Deals Available, {email['firstName']}!\n\n{email_message}".encode('utf-8')
                )
