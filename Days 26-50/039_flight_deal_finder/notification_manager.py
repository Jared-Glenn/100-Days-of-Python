from twilio.rest import Client
import security

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.api_key = security.TWILIO_API_KEY
        self.auth_token = security.TWILIO_AUTH_TOKEN
        self.acct_sid = security.TWILIO_ACCT_SID

    def send_message(self, deal_list):
        for deal in deal_list:
            low_price_alert = f"Low price alert! Only £{deal['price']} to fly from " \
                              f"{deal['dep_city']}-{deal['dep_aita_code']} to " \
                              f"{deal['arr_city']}-{deal['arr_aita_code']}, from " \
                              f"{deal['out_date']} to {deal['in_date']}."

            client = Client(self.acct_sid, self.auth_token)

            message = client.messages \
                .create(
                    body=low_price_alert,
                    from_="+15618234125",
                    to="+14355123350"
                )
            print(message.status)
