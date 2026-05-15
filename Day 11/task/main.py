from art import logo
import random

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
NO_CARD = "no_card"

def blackjack_game():
    player_cards, computer_cards = set_up()
    player_points = calculate_points(player_cards)
    # Player turn
    choice = "y"
    while choice == "y":
        print_menu(player_cards, computer_cards, hide_computer_card=True)
        choice = input("Would you like another card? (y/n): ").lower()
        if choice == "y":
            player_cards.append(draw_card(True))

        player_points = calculate_points(player_cards)
        if player_points > 21:
            dealer_wins("You busted!")
            return
        elif player_points == 21:
            player_wins("BLACKJACK!")
            return



    # Dealer turn
    computer_points = calculate_points(computer_cards)
    while computer_points < 16 or computer_points < player_points:
        print_menu(player_cards, computer_cards, hide_computer_card=False)
        computer_cards.append(draw_card(True))

        computer_points = calculate_points(computer_cards)

    print_menu(player_cards, computer_cards, hide_computer_card=False)
    if computer_points > 21:
        player_wins("Dealer busted!")
        return
    if computer_points > player_points:
        dealer_wins("Dealer beat you!")
        return



def draw_card(confirm_needed=False):
    new_card = random.choice(cards)
    if confirm_needed:
        input(f"Drew Card: {new_card}\nPress Enter to continue...")
    return new_card

def calculate_points(card_list):
    points = 0
    aces = 0
    for card in card_list:
        if card == "A":
            aces += 1

        points += card_values[cards.index(card)]

    while points > 21 and aces > 0:
        points -= 10
        aces -= 1

    return points

def set_up():
    player_cards = []
    computer_cards = []

    # Starting hand
    player_cards.append(draw_card())
    player_cards.append(draw_card())

    computer_cards.append(draw_card())
    computer_cards.append(draw_card())
    return player_cards, computer_cards

def print_menu(player_cards:list, computer_cards:list, hide_computer_card=True):
    print(logo)

    computer_hand = computer_cards if not hide_computer_card else [computer_cards[0], "-"]
    computer_points = calculate_points(computer_cards) if not hide_computer_card else calculate_points([computer_cards[0]])

    print(f"Dealer hand: {computer_hand}")
    print(f"Dealer points: {computer_points}")

    print("\n" * 3)

    print(f"Player hand: {player_cards}")
    print(f"Player points: {calculate_points(player_cards)}")


def player_wins(message):
    print(message)
    print("You won!")

def dealer_wins(message):
    print(message)
    print("Dealer wins!")

replay = True
while replay:
    blackjack_game()
    replay = input("Want to play again? (y/n): ").lower() == "y"