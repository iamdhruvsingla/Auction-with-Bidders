from auction_art import logo
print(logo)
import os

def clear():
    if os.name != "nt":
        os.system('clear')

# FIRST TRY
# names_and_bids = {}

# # def bid():
# #     name = input("Enter your name\n")
# #     bid_price = input("Enter your bid price\n")
# #     names_and_bids[name]= bid_price
# #     more_players = input("Is there anyone else who wants to bid? yes or no\n").lower()
# #     if more_players == "yes":
# #         bid()
# #     else:
# #         for names in names_and_bids:
# #             bids = names_and_bids[names]
# #             bids_array = []
# #             bids_array.append(bids)
# #             highest = str(0)
# #             for i in range(0, len(bids_array)):
# #                 if bids_array[i] > highest:
# #                     highest = bids_array[i]
# #     print(f"Highest bid is {highest}")
# # bid()


# SECOND TRY
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