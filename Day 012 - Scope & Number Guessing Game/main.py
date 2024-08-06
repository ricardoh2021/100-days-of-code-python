from art import logo
import random

EASY_GAME_GUESSES = 10
HARD_GAME_GUESSES = 5

def guessing_game(difficulty):
    """
    Play a number guessing game based on the chosen difficulty level.

    Args:
    difficulty (str): The difficulty level of the game, either 'easy' or 'hard'.

    The game allows the player a certain number of guesses to find a randomly generated number
    between 1 and 100. The number of guesses depends on the difficulty level:
    - Easy: 10 guesses
    - Hard: 5 guesses

    The player is prompted to guess the number, and feedback is provided whether the guess is too high or too low.
    The game ends when the player correctly guesses the number or runs out of guesses.
    """
    if difficulty == 'easy':
        guesses = EASY_GAME_GUESSES
    else:
        guesses = HARD_GAME_GUESSES

    numberToGuess = random.randint(1, 100)

    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        while True:
            try:
                guess = int(input("Make a guess: "))
                break  # Exit the loop if the input is a valid integer
            except ValueError:
                print("Invalid Input. Please make another guess: ")
        # Compare the guess with the target number
        if guess == numberToGuess:
            print(f"Congratulations! You guessed the number! It was {numberToGuess}")
            exit()
        elif guess > numberToGuess:
            print("Too High.")
        elif guess < numberToGuess:
            print("Too low.")
        print("Guess Again.\n")
        guesses -= 1

    print("You have run out of guesses😭. You lose")
    exit()

# Main game execution
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()

while difficulty not in ['easy', 'hard']:
    difficulty = input("Invalid Input. Please type 'easy' or 'hard': ").strip().lower()

guessing_game(difficulty)