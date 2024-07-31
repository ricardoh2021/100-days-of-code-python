


import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["-"] * len(chosen_word)

game_playing = True

lives = 6

while game_playing:
    user_guess = input("Guess a letter: ").lower()

    if len(user_guess) == 1 and user_guess.isalpha():
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        letterGuessed = False

        for position in range(0, len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_guess:
                display[position] = letter
                letterGuessed = True

        #TODO-2: - If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        if letterGuessed == False:
            lives = lives - 1
            print(f"Incorrect Guess! You have {lives} lives left.")

            if lives == 0:
                print("Game over. No more lives left:")
                print(stages[lives])
                game_playing = False

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
        print(stages[lives])

        #Check the list if it contains "-"
        if display.count("-") == 0:
            print("Game has ended! Congratulations!")
            game_playing = False
    else:
        print("Invalid Input: Please guess only a letter.")
        continue

