import requests
import datetime as dt
import security

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.headers = {
            "apikey": security.KIWI_API_KEY,
        }
        self.deal_list = []

    def search_flights(self, sheet_length, destination_data):
        tmrw = dt.datetime.now() + dt.timedelta(days=1)
        tomorrow = tmrw.strftime("%d/%m/%Y")
        six_months = dt.datetime.now() + dt.timedelta(days=180)
        six_months_date = six_months.strftime("%d/%m/%Y")

        # for i in range(sheet_length):
        for i in range(1):
            data = {
                "fly_from": "LON",
                "fly_to": destination_data[i]["iataCode"],
                "dateFrom": tomorrow,
                "dateTo": six_months_date,
                "cur": "GBP",
                # "price_to": destination_data[i]["lowestPrice"],
                "sort": "price",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "limit": 1,
            }

            response = requests.get(url=self.endpoint, headers=self.headers, params=data)
            response.raise_for_status()

            if response.json()["_results"] > 1:
                out_date = response.json()["data"][0]["route"][0]["local_departure"].split("T")[0]
                in_date = response.json()["data"][0]["route"][1]["local_departure"].split("T")[0]
                self.deal_list.append({
                    "price": response.json()["data"][0]["price"],
                    "dep_city": response.json()["data"][0]["cityFrom"],
                    "dep_aita_code": response.json()["data"][0]["flyFrom"],
                    "arr_city": response.json()["data"][0]["cityTo"],
                    "arr_aita_code": response.json()["data"][0]["flyTo"],
                    "out_date": out_date,
                    "in_date": in_date,
                })

        return self.deal_list
