import random

from game_data import data


def higher_lower_game():
    options = [get_data(), get_data()]
    answer = 0 if options[0]["follower_count"] > options[1]["follower_count"] else 1

    while options[0] == options[1]:
        options[1] = get_data()

    print_options_data(options)
    guess = get_guess()

    if guess == answer:
        print("Correct!")
    else:
        print("Wrong!")

    return





def get_data():
    return random.choice(data)

def print_options_data(options):
    for index, opt in enumerate(options):
        print(f"{index}) {opt['name']}, a {opt["description"]} from {opt['country']}")

def get_guess():
    return input("Enter your guess: ").lower()



higher_lower_game()