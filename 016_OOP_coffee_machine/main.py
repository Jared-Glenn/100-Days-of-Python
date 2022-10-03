from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()

running = True

while running:
    money = MoneyMachine()
    command = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if command == "off":
        running = False
    elif command == "report":
        maker.report()
    elif command in ["espresso", "latte", "cappuccino"]:
        order = menu.find_drink(command)
        if not money.make_payment(order.cost):
            print("Sorry, that's not enough money. Money refunded.")
            continue
        if maker.is_resource_sufficient((order)):
            maker.make_coffee(order)
    else:
        print("Please enter a valid response.")

print("Thank you! Come again!")
