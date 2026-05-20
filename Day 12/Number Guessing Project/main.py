from art import logo
import random

DIFFICULTY = {
    "easy": 20,
    "medium": 10,
    "hard": 5,
}

def guessing_game():
    answer = random.randint(1,101)
    print(f"Hint: {answer}")
    print(logo)

    max_tries = set_difficulty()
    tries = 0
    guess = -1


    while tries != max_tries and guess != answer:
        guess = int(input("Guess the number: "))
        if guess == answer:
            print("You guessed the number!")
            return

        elif guess > answer:
            print("It's too high.")
        else:
            print("It's too low.")

        tries += 1

    print("You run out of tries!")
    print(f"The answer was {answer}...")
    return


def set_difficulty():
    print("Choose a difficulty: Easy, Medium, Hard")
    difficulty = input("Difficult: ").lower()

    return DIFFICULTY[difficulty]

def retry_game(game):
    while input("Do you want to try again?(y/n)").lower() == "y":
        game()

guessing_game()
retry_game(guessing_game)