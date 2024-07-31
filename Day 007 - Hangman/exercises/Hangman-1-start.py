#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while True:

    user_guess = input("Guess a a letter:\n").lower()

    ##Check if input is a letter and has length of 1
    if len(user_guess) == 1 and user_guess.isalpha():
        #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        for c in random_word:
            if user_guess == c:
                print("True")
            else:
                print("False")
        break
    else:
        print("Invalid Input: Please guess only a letter.")
        continue

