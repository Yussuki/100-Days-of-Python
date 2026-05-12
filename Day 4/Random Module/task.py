import random

print("Welcome to the game!")
choice = input("Do you choose Heads or Tails?")

result = "Heads" if random.randint(0,1) else "Tails"

if choice == result:
    print("You won!")
else:
    print(f"Sorry, the coin flipped {result}...")