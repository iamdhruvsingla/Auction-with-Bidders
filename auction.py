from auction_art import logo
print(logo)
import os

def clear():
    if os.name != "nt":
        os.system('clear')

bids = {}
bidding_finished = False

def highest():
    highest = str(0)
    for names in bids:
        if bids[names] > highest:
            highest = bids[names]
            winner = names
    print(f"highest bid is by {winner} of {highest}")

while not bidding_finished:
    name = input("Enter your name\n")
    price = input("Enter your bid price\n")
    bids[name] = price
    more_players = input("Are there any more Bidders? yes or no\n").lower()
    if more_players == "no":
        bidding_finished = True
        highest()
    elif more_players == "yes":
        clear()
