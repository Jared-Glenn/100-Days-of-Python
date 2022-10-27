#This class is responsible for talking to the Google Sheet.
import requests
import security

class DataManager:

    def __init__(self):
        self.flight_endpoint = security.FLIGHT_SHEETY_ENDPOINT
        self.customer_endpoint = security.USER_SHEETY_ENDPOINT
        self.sheet_length = None
        self.destination_data = None
        self.headers = {
            "Authorization": security.SHEETY_AUTH
        }

    def get_destination_data(self):
        response = requests.get(url=self.flight_endpoint, headers=self.headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        self.sheet_length = len(response.json()["prices"])

    def input_city_codes(self, iata_list):
        for i in range(self.sheet_length):
            data = {
                "price": {
                    "iataCode": iata_list[i]
                }
            }
            this_endpoint = f"{self.flight_endpoint}/{i + 2}"
            response = requests.put(url=this_endpoint, headers=self.headers, json=data)
            print(response.text)


    def get_emails(self):
        response = requests.get(url=self.customer_endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()["users"]

