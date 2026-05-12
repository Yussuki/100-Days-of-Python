print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


def game_over():
    print("Game Over x.x")

def make_a_choice(options: list) -> str:

    for i,option in enumerate(options):
        print(f"{i+1} - {option}")

    return input("Choice: ")

def game():
    print("Do you go left or right?")
    if make_a_choice(["left", "right"]) != "left":
        print("You fell into a hole...")
        game_over()
        return

    print("You find a house, but there way is blocked by the sea.")
    print("Do you wait or try to swim?")
    if make_a_choice(["swim", "wait"]) != "wait":
        print("You try to swim but is attacked by a trout...")
        game_over()
        return

    print("After a while waiting, the sea level decreases and you get to reach the house.")
    print("Inside the house, you find three doors, a red one, a blue one and a yellow one, which one do you try?")
    match make_a_choice(["red", "blue", "yellow"]):
        case "red":
            print("You trigger a fire trap and is burned crisped!")
            game_over()
            return
        case "blue":
            print("You fell in a den of beasts and is eaten...")
            print("Who left that hole there?..")
            game_over()
            return

        case "yellow":
            print("Congratulations, you found the treasure chest!!!")
            return

        case _:
            print("While deciding, the house collapsed above you")
            game_over()
            return

game()