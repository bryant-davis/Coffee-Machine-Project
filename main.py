# TODO: Add try catch for error handling

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

valid_options = ["espresso", "latte", "cappuccino", "off", "report"]

def get_input():
    selection = input("What would you like? (espresso/latte/cappuccino):  ")
    if selection not in valid_options:
        print("That is an invalid option, please try again.")
        run_program()
    if selection == "off":
        exit()
    if selection == "report":
        print_report()
        run_program()
    return selection

def print_report():
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')

def check_resources(user_drink):
    if MENU[user_drink]["ingredients"]["water"] > resources["water"]:
        print("sorry, not enough water")
        return False
    elif MENU[user_drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("sorry, not enough water")
        return False
    elif user_drink != "espresso" and MENU[user_drink]["ingredients"]["milk"] > resources["milk"]:
        print("sorry, not enough water")
        return False
    else:
        return True

def process_coins():
    total = 0
    num_quarters = int(input("Enter number of quarters.  "))
    num_dimes = int(input("Enter number of dimes.  "))
    num_nickels = int(input("Enter number of nickels.  "))
    num_pennies = int(input("Enter number of pennies.  "))
    
    total += num_quarters * 0.25
    total += num_dimes * 0.10
    total += num_nickels * 0.05
    total += num_pennies * 0.01
    print(f'Money deposited: ${total:.2f}')
    return total

def validate_transaction(money_deposited, user_drink):
    if MENU[user_drink]["cost"] > money_deposited:
        print("Sorry, that's not enough money. Money refunded.")
        run_program()
    else:
        change_to_dispense = money_deposited - MENU[user_drink]["cost"]
        resources["money"] += (money_deposited - change_to_dispense)
        print(f'Change returned: ${change_to_dispense:.2f}')

def make_coffee(user_drink):
    resources["water"] -= MENU[user_drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
    if user_drink != "espresso":
        resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
    print(f'Here is your {user_drink}. Enjoy!')

def run_program():
    user_drink = get_input()
    if check_resources(user_drink) is True:
        print(f'Please depost ${MENU[user_drink]["cost"]:.2f}')
        money_deposited = process_coins()
        validate_transaction(money_deposited, user_drink)
        make_coffee(user_drink)

run_program()
