import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def game():
    choices = [rock, paper, scissors]

    pc_choice = random.choice(choices)
    player_choice = input("You choose rock, paper or scissors: ")
    if player_choice == "rock":
        player_choice = choices[0]

    elif player_choice == "paper":
        player_choice = choices[1]

    elif player_choice == "scissors":
        player_choice = choices[2]

    else:
        print("Invalid choice")
        return

    print(f"Your choice\n{player_choice}\n\n")
    print(f"Opponent's choice\n{pc_choice}\n\n")
    if player_choice == pc_choice:
        print("Draw")
        return

    if (player_choice == rock and pc_choice == scissors) or \
        (player_choice == scissors and pc_choice == paper) or \
            (player_choice == paper and pc_choice == rock):
        print("You win")
        return

    print("You lose")

game()