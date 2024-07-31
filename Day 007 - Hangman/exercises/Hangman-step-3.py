


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



#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#Step 2

while game_playing:
    user_guess = input("Guess a letter: ").lower()

    if len(user_guess) == 1 and user_guess.isalpha():
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        for position in range(0, len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_guess:
                print("Right")
                display[position] = letter
            else:
                print("Wrong")
        print(display)
        #Check the list if it contains "-"
        if display.count("-") == 0:
            print("Game has ended! Congratulations!")
            break
    else:
        print("Invalid Input: Please guess only a letter.")
        continue

