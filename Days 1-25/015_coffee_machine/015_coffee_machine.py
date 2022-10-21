MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def add_money():
    coins = {
        "quarters" : 0.25,
        "dimes" : 0.1,
        "nickles" : 0.05,
        "pennies" : 0.01,}
    total = 0
    print("Please insert coins.")
    for coin in coins:
        c = input(f"How many {coin}? ")
        try:
            total += (int(c) * coins[coin])
        except:
            pass
    resources["money"] = total


def print_menu():
    print("---- MENU ----")
    for coffee in MENU:
        cost = "${:,.2f}".format(MENU[coffee]['cost'])
        print(f"{coffee.capitalize()}:", cost)


def check_ingred(coffee):
    stocked = True
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        stocked = False
        print("Sorry, there is not enough water.")
    if "milk" in MENU[coffee]["ingredients"] and resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
        stocked = False
        print("Sorry, there is not enough milk.")
    if resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        stocked = False
        print("Sorry, there is not enough coffee.")
    if resources["money"] < MENU[coffee]["cost"]:
        stocked = False
        print("Sorry, that's not enough money. Money refunded.")
    return stocked


running = True
resources["money"] = 0

while running:
    print_menu()
    coffee = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if coffee == "off":
        running = False
    elif coffee == "report":
        for resource in resources:
            print(f"{resource.capitalize()}: {resources[resource]}")
    elif coffee in MENU:
        add_money()
        if check_ingred(coffee):
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            if "milk" in MENU[coffee]["ingredients"]:
                resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            resources["money"] -= MENU[coffee]["cost"]
            print("Your change is ${:,.2f}".format(resources['money']))
            print(f"Here's your {coffee}! Enjoy!")
        resources["money"] = 0
    else:
        print("Please enter a valid response.")

print("Thank you! Come again!")