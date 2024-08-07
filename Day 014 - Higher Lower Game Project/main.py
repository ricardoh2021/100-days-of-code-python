import random 
from art import logo, vs
from game_data import data
import os

# Get two random people to start with for A and B from dictionary data
data_A = random.choice(data)
data_B = random.choice(data)

while data_B == data_A:
    data_B = random.choice(data)

score = 0

def print_game_info(increaseScore):
    """
    Prints the current game information including the current score if applicable.
    
    Args:
        increaseScore (bool): Flag to indicate if the score should be displayed.
    
    """
    print(logo)
    if increaseScore:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {data_A.get('name')}, a {data_A.get('description')}, from {data_A.get('country')}\n")
    print(vs)
    print(f"Compare B: {data_B.get('name')}, a {data_B.get('description')}, from {data_B.get('country')}")

def follower_question_prompt():
    """
    Prompts the user to guess which person has more followers.
    
    Returns:
        str: The user's choice ('a' or 'b') indicating their guess.
    
    """
    followerQuestion = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    while followerQuestion not in ['a', 'b']:
        followerQuestion = input("Invalid Input. Please try again.\nWho has more followers? Type 'A' or 'B': ").strip().lower()
    return followerQuestion

def compare_followers(userChoice):
    """
    Compares the follower counts of the two people and updates the game state.
    
    Args:
        userChoice (str): The user's choice ('a' or 'b') indicating their guess.
    
    Returns:
        bool: True if the user's guess is correct, False otherwise.
    
    """
    global score, data_A, data_B
    followerCountA = int(data_A.get("follower_count"))
    followerCountB = int(data_B.get("follower_count"))
    isCorrect = followerCountA > followerCountB  # Default. We assume player chooses A

    if userChoice == 'b':
        isCorrect = followerCountB > followerCountA
    if isCorrect:
        score += 1
        data_A = data_B
        data_B = random.choice(data)
        while data_B == data_A:
            data_B = random.choice(data)
    else:
        return False
    os.system('clear')
    print_game_info(True)
    return True

def playHigherLower():
    """
    Starts and manages the main game loop.
    """
    continueGame = True
    print_game_info(False)
    while continueGame:
        userChoice = follower_question_prompt()
        continueGame = compare_followers(userChoice)
    os.system('clear')
    print(logo)
    print(f"Sorry that's wrong. Your final score: {score}")

playHigherLower()