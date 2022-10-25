import requests
import datetime as dt
import security

NIX_APP_ID = security.NIX_APP_ID
NIX_API_KEY = security.NIX_API_KEY

SHEETY_AUTH = security.SHEETY_AUTH

EXERCISE_NIX_ENDPOINT = security.EXERCISE_NIX_ENDPOINT
EXERCISE_SHEETY_ENDPOINT = security.EXERCISE_SHEETY_ENDPOINT

nix_headers = {
    "x-app-id": NIX_APP_ID,
    "x-app-key": NIX_API_KEY,
    "Content-Type": "application/json"
}

sheety_headers = {
    "Authorization": SHEETY_AUTH,
}



query = input("What exercises did you do?")


parameters = {
    "query": query,
}

nix_response = requests.post(url=EXERCISE_NIX_ENDPOINT, json=parameters, headers=nix_headers)

now = dt.datetime.now()

for i in range(len(nix_response.json()["exercises"])):

    sheety_parameters = {
        "workout": {
            "date": now.strftime("%m/%d/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": (nix_response.json()["exercises"][i]["name"]).title(),
            "duration": nix_response.json()["exercises"][i]["duration_min"],
            "calories": nix_response.json()["exercises"][i]["nf_calories"],
        }
    }

    sheety_response = requests.post(url=EXERCISE_SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    sheety_response.raise_for_status()
    print(sheety_response)
