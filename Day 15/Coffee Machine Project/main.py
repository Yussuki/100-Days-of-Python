from typing import Any
from unittest import case

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
    "money": 0.0,
}

measurements = {
    "liquids": ["water", "milk"],
    "solids": ["coffee"],
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}



def coffe_machine():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        return False
    elif order == "report":
        get_report()
    else:
        process_order(order)
        return True

    return True

def get_report():
    for key, value in resources.items():
        if key in measurements["liquids"]:
            print(f"{key.capitalize()}: {value}ml")
        elif key in measurements["solids"]:
            print(f"{key.capitalize()}: {value}g")
        else:
            print(f"{key.capitalize()}: ${value:.2f}")


def check_ingredients(order):
    for ingredient_name, ingredient_quantity in MENU[order]["ingredients"].items():
        if resources[ingredient_name] < ingredient_quantity:
            print(f"Sorry, there is not enough {ingredient_name}.")
            return False

    return True

def process_order(order):
    if not check_ingredients(order):
        return

    if not process_payment(order):
        return

    update_resources(order)
    print(f"Here is your {order}! Enjoy!")
    return

def process_payment(order):
    cost = MENU[order]["cost"]
    payment = 0
    for coin, value in coins.items():
        payment += int(input(f"How many {coin} do you insert? (${value:.2f}) ")) * value

    if payment < cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif payment > cost:
        change = payment - cost
        print(f"Here is ${change:.2f} in change.")
    return True

def update_resources(order):
    global resources

    resources["money"] += MENU[order]["cost"]
    for ingredient_name, ingredient_quantity in MENU[order]["ingredients"].items():
        resources[ingredient_name] -= ingredient_quantity

    return

repeat = True
while repeat:
    repeat = coffe_machine()
