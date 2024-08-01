from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bidders = {}
stillBidding = True


def add_bidder(name, bid):
  bidders[name] = bid


def check_winner():
  higest_bid = 0
  winner = ""
  for bidder in bidders:
    if bidders[bidder] > higest_bid:
      higest_bid = bidders[bidder]
      winner = bidder
  return winner


print(logo)
print("Welcome to the secret auction program. \n")

while stillBidding:
  name = input("What is your name?:\n")
  bid = int(input("What's your bid? $\n"))
  add_bidder(name, bid)
  continueBidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if continueBidding == 'no':
    stillBidding = False
    print(
        f"The winner is {check_winner()} with a bid of ${bidders[check_winner()]}"
    )
  else:
    clear()
