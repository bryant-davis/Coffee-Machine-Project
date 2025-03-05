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
    "money": 0.00
}

def get_input():
    selection = input("What would you like? (espresso/latte/cappuccino):")
    if selection == "off":
        exit()
    if selection == "report":
        print_report()
        exit()
    return selection

def print_report():
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')

def check_resources(user_drink):
    if MENU[user_drink]["ingredients"]["water"] > resources["water"]:
        print("sorry, not enough water")
    elif MENU[user_drink]["ingredients"]["milk"] > resources["milk"]:
        print("sorry, not enough water")
    elif MENU[user_drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("sorry, not enough water")
    else:
        return True

def process_coins():
    total = 0
    num_quarters = int(input("Enter number of quarters."))
    num_dimes = int(input("Enter number of dimes."))
    num_nickels = int(input("Enter number of nickels."))
    num_pennies = int(input("Enter number of pennies."))
    
    total += num_quarters * 0.25
    total += num_dimes * 0.10
    total += num_nickels * 0.05
    total += num_pennies * 0.01
    return total

def validate_transaction(money_deposited, user_drink):
    if MENU[user_drink]["cost"] > money_deposited:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        change_to_dispense = money_deposited - MENU[user_drink]["cost"]
        resources["money"] += (money_deposited - change_to_dispense)
        print(resources["money"])

def make_coffee(user_drink):
    resources["water"] -= MENU[user_drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
    if user_drink != "espresso":
        resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
    print(resources)
    print(f'Here is your {user_drink}. Enjoy!')

