import requests
from datetime import datetime, timedelta
import random

USERNAME = "jaredglenn"
TOKEN = "uZ*AxIM!a7xkT3"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Daily Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()

graph1_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?"),
}


graph1_endpoint = f"{graph_endpoint}/graph1"

response = requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)
print(response.text)

# for day in range(360):
#
#     today = (datetime.now()-timedelta(day)).strftime("%Y%m%d")
#
#     qty = str(random.choice(range(30, 150, 10)))
#
#     activity_params = {
#         "date": today,
#         "quantity": qty
#     }
#
#     response = requests.post(url = graph1_endpoint, json=activity_params, headers=headers)
#     print(response.text)


change_endpoint = f"{graph1_endpoint}/{today.strftime('%Y%m%d')}"

change_config = {
    "quantity": "120",
}

# response = requests.put(url=change_endpoint, json=change_config, headers=headers)
# print(response.text)

# response = requests.delete(change_endpoint, headers=headers)
# print(response.text)