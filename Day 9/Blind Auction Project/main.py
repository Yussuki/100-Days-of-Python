# TODO-1: Ask the user for input
def get_input(bids):
    name = input("Please enter your name: ")
    bid_amount = float(input("Please enter your bid amount: "))
    bids[name] = bid_amount
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def get_buyer(bid_dict):
    highest_bid = 0
    buyer = ""
    for key, value in bid_dict.items():
        if value > highest_bid:
            highest_bid = value
            buyer = key

    return buyer


bids = {}
more_participants = True
while more_participants:
    get_input(bids)
    more_participants = input("Would you like to see more participants? (y/n): ") == "y"
    print("\n" * 20)

buyer = get_buyer(bids)
print(f"{buyer}'s bid won the auction!")