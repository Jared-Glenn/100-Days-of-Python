#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
# flight_search = FlightSearch()

flight_data = FlightData()
notification_manager = NotificationManager()

data_manager.get_destination_data()
# flight_search.search_iata(data_manager.sheet_length, data_manager.destination_data)
# data_manager.input_city_codes(flight_search.iata_list)

deal_list = flight_data.search_flights(data_manager.sheet_length, data_manager.destination_data)

if len(deal_list) >= 1:
    notification_manager.send_message(deal_list)

# print(data_manager.destination_data)
