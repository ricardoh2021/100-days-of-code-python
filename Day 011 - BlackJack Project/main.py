############### Blackjack Project #####################
from art import logo
import random

############### Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# Jack/Queen/King count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# Constants for card values
CARD_VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 

def get_user_input(prompt):
    """
    Prompt the user for input and validate the response.
    
    Args:
    - prompt (str): The prompt message to display.
    
    Returns:
    - response (str): The validated user input, either 'y' or 'n'.
    """
    response = input(prompt).strip().lower()
    while response not in ['y', 'n']:
        response = input("Invalid input. Please type 'y' or 'n': ").strip().lower()
    return response

def deal_computer_cards():
    """
    Deal cards to the computer (dealer) until the sum is at least 17.
    
    Returns:
    - dealer_cards (list): The list of cards dealt to the dealer.
    """
    dealer_cards = []
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(CARD_VALUES))
    return dealer_cards

def starting_user_hand():
    """
    Deal the initial two cards to the user.
    
    Returns:
    - user_cards (list): The initial two cards dealt to the user.
    """
    return [random.choice(CARD_VALUES) for _ in range(2)]

def deal_user_card(user_cards):
    """
    Deal an additional card to the user.
    
    Args:
    - user_cards (list): The current list of cards held by the user.
    """
    user_cards.append(random.choice(CARD_VALUES))

def print_final_scores(user_cards, dealer_cards, user_score, dealer_score):
    """
    Print the final scores of the user and the dealer.
    
    Args:
    - user_cards (list): The list of cards held by the user.
    - dealer_cards (list): The list of cards held by the dealer.
    - user_score (int): The user's final score.
    - dealer_score (int): The dealer's final score.
    """
    print(f"  Your Final cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's Final cards: {dealer_cards}, final score: {dealer_score}")

def play_blackjack():
    """
    Play a single session of Blackjack.
    """
    print(logo)
    user_cards = starting_user_hand()
    user_score = sum(user_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    dealer_cards = deal_computer_cards()
    dealer_first_card = dealer_cards[0]
    print(f"    Computer's first card: {dealer_first_card}")

    keep_dealing = True

    while keep_dealing and user_score <= 21:
        another_card = get_user_input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == 'y':
            deal_user_card(user_cards)
            user_score = sum(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {dealer_first_card}")
        else:
            keep_dealing = False

    if user_score > 21:
        print_final_scores(user_cards, dealer_cards, user_score, sum(dealer_cards))
        print("You went over. You lose😭")
    else:
        dealer_score = sum(dealer_cards)
        print_final_scores(user_cards, dealer_cards, user_score, dealer_score)
        if dealer_score > 21 or user_score > dealer_score:
            print("You WIN!🎉")
        elif user_score == dealer_score:
            print("It's a draw!🫠")
        else:
            print("You lose!💀")

# Main game loop
game_session = get_user_input("Do you want to start a game of Blackjack? Type 'y' or 'n': ")
while game_session == 'y':
    play_blackjack()
    game_session = get_user_input("Do you want to play again? Type 'y' or 'n': ")

print("Exiting the game")


####### Original Code below used in ChatGPT to get to above code #############
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #Cards not removed from the deck 
# gameSession = input("Do you want to stat a game of Blackjack? Type 'y' or 'n': ").strip().lower()
# userCards = []
# sumOfUser = 0
# sumOfDealer = 0

# def dealComputerCards():
#     dealerCards = []
#     card = random.choice(cards)
#     while sum(dealerCards) + card < 21:
#         #Add the card
#         dealerCards.append(card)
#         card = random.choice(cards)
#     if(len(dealerCards) == 2 and sum(dealerCards) < 17):
#         card = random.choice(cards)
#         dealerCards.append(card)
#     return dealerCards

# def startingUserHand():
#     ##First two cards 
#     firstUserCard = random.choice(cards)
#     secondUserCard = random.choice(cards)
#     userCards.append(firstUserCard)
#     userCards.append(secondUserCard)

# def dealUserCard():
#     card = random.choice(cards)
#     userCards.append(card)

# while gameSession not in ['y', 'n']:
#     gameSession = input("Invalid Inpput. PLEASE Type 'y' or 'n': ").strip().lower()

# if gameSession == 'y':
#     print(logo)
#     startingUserHand()
#     sumOfUser += sum(userCards)
#     print(f"    Your cards: {userCards}, current score: {sumOfUser}")
#     dealerCards = dealComputerCards()
#     dealerFirstCard = dealerCards[0]
#     print(f"    Computer's first card: {dealerFirstCard}")


#     ## While user continues to deal hands until satisfied or it is over 21, then game ends.
#     keepDealing = True

#     if(sumOfUser > 21):
#         print(f"  Your Final cards: {userCards}, current score: {sumOfUser}")
#         print(f"  Computer's Final card: {dealerFirstCard}, final score: {dealerFirstCard}")
#         print("You went over. You lose😭")
#         keepDealing = False
#     while keepDealing:
#         anotherCard = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()

#         if anotherCard == 'y':
#             dealUserCard()
#             sumOfUser = sum(userCards)
#             print(f"    Your cards: {userCards}, current score: {sumOfUser}")
#             print(f"    Computer's first card: {dealerFirstCard}")

#             if(sumOfUser > 21):
#                 ##End the game and exit
#                 keepDealing = False
#                 print(f"  Your Final cards: {userCards}, current score: {sumOfUser}")
#                 print(f"  Computer's Final card: {dealerFirstCard}, final score: {dealerFirstCard}")
#                 print("You went over. You lose😭")
#         else:
#             keepDealing = False
#             sumOfDealer = sum(dealerCards)
#             print(f"  Your Final cards: {userCards}, current score: {sumOfUser}")
#             print(f"  Computer's Final card: {dealerCards}, final score: {sumOfDealer}")

#             if sumOfDealer > 21:
#                 print("You WIN!🎉")
#             elif(sumOfUser > sumOfDealer):
#                 print("You WIN!🎉")
#             elif sumOfUser == sumOfDealer:
#                 print("It's' a draw!🫠")
#             else:
#                 print("You lose!💀")


        
        
        


# elif gameSession == 'n':
#     print("exiting the game")