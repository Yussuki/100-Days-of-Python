print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

def calculate_cost(size, pepperoni, extra_cheese):
    match size:
        case "S":
            cost = 15
        case "M":
            cost = 20
        case "L":
            cost = 25
        case _:
            print("Sorry, that's not a valid size.")
            return

    if pepperoni == "Y":
        if size == "S":
            cost += 2
        else:
            cost += 3

    if extra_cheese == "Y":
        cost += 1

    print(f"Your final bill is: ${cost}.")

calculate_cost(size, pepperoni, extra_cheese)