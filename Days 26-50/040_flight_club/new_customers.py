import requests
import security


print("Welcome to Jared's Flight Club")
print("We find the best flight deals and email them to you!")
first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is your email address?")
validation_email = input("Please input your email again (for verification).")

while email != validation_email:
    print("Those emails did not match.")
    print("Let's start that process over.")
    email = input("What is your email address?")
    validation_email = input("Please input your email again (for verification).")

headers = {
    "Authorization": security.SHEETY_AUTH
}

data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}

response = requests.post(url=security.USER_SHEETY_ENDPOINT, json=data, headers=headers)
print(response.text)

print("Congratulations! You're in the club!")