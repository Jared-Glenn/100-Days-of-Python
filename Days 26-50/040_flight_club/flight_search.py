# This class is responsible for talking to the Flight Search API.
import requests
import security

class FlightSearch:

    def __init__(self):
        self.headers = {
            "apikey": security.KIWI_API_KEY,
        }
        self.flight_search_endpoint = "https://tequila-api.kiwi.com/locations/query"
            #"https://api.tequila.kiwi.com/v2/search"
        self.iata_list = []


    def find_city(self):
        parameters = {
            "term": "New York",
            "location_types": "city"
        }

        response = requests.get(url=self.flight_search_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        print(response.text)

    def search_iata(self, list_length, city_list):
        for i in range(list_length):
            parameters = {
                "term": city_list[i]["city"],
                "location_types": "city"
            }
            response = requests.get(url=self.flight_search_endpoint, params=parameters, headers=self.headers)
            response.raise_for_status()
            self.iata_list.append(response.json()["locations"][0]["code"])




