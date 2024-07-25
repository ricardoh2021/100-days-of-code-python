import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

while True:
    playerChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n")

    if playerChoice.isdigit():
        number = int(playerChoice)
        if 0 <= number <= 2:
            randIntForComp = random.randint(0, len(choices) - 1)
            print(f"You chose:\n{choices[number]}")
            print(f"Computer chose:\n{choices[randIntForComp]}")

            if number == randIntForComp:
                print("It's a draw!")
            elif (number == 0 and randIntForComp == 2) or (number == 1 and randIntForComp == 0) or (number == 2 and randIntForComp == 1):
                print("You win!")
            else:
                print("You lose!")
        else:
            print("The number is out of the allowed range (0-2).")
    else:
        print("Invalid input. Please enter an integer.")

    play_again = input("Do you want to play again? Type 'yes' to continue or anything else to exit: ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break