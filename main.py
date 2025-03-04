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
# water == 300
resources = {
    "water": 0,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}

# Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# Turn off the machine by user entering "off" to the prompt"
def get_input():
    selection = input("What would you like? (espresso/latte/cappuccino):")
    if selection == "off":
        exit()
    if selection == "report":
        print_report()
        exit()
    return selection
# Print report. If user enters "report" then available resources should print (Water: xxxml Milk: xxml Coffee: xxg Money: $x.x)
def print_report():
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')
# Check resources function. Before dispensing it needs to validate that there's enough resources
def check_resources(user_drink):
    if MENU[user_drink]["ingredients"]["water"] > resources["water"]:
        print("sorry, not enough water")
    elif MENU[user_drink]["ingredients"]["milk"] > resources["milk"]:
        print("sorry, not enough water")
    elif MENU[user_drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("sorry, not enough water")
    else:
        return True
# Process coins function. 
#   If sufficient resources, user should be prompted to enter coins and function stores how much money was deposited. 
def process_coins():
    num_quarters = int(input("Enter number of quarters."))
# Function to validate transaction successful.
#   Check sufficient money deposited. If not, "Sorry that's not enough money. Money refunded." 
#   If enough money deposited, this money is added to Report money. 
#   Change is dispensed. 
# Function to make coffee
#   Resources deducted
#   Print “Here is your {latte}. Enjoy!"

print_report()
user_selection = get_input()
check_resources(user_selection)