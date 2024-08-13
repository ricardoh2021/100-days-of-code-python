# Day 14 - 100 Days of Code: Learning Python

## Higher Lower Game

Today, I created a Higher Lower game in Python. Initially, I coded the brute force version of the game. This approach allowed me to get the core functionality working before refactoring the code to improve its structure and readability.

### Key Learnings

1. **Breaking Down Code into Functions**:

   - I started by writing the game in a single block of code. Once it was working, I broke it down into smaller, more manageable functions. This made the code more modular and easier to understand.

2. **Avoiding Global Variables**:

   - In my initial version, I used global variables to keep track of the game state. After checking my code with the refactored version from ChatGPT, I realized that using global variables, especially when they are not constants, is not a good practice. It can lead to bugs and makes the code harder to maintain.
   - Instead, I passed variables as arguments to functions and returned values as needed. This approach made the code cleaner and more reliable.

3. **Reducing Redundancy**:
   - The refactored version from ChatGPT also highlighted areas where I had redundant code. By refactoring, I was able to reduce this redundancy, making the code more efficient and easier to read.

### Refactored Code

Here is the refactored version of my Higher Lower game, with improvements for modularity, readability, and efficiency:

```python
import random
from art import logo, vs
from game_data import data
import os

def get_random_data(exclude=None):
    item = random.choice(data)
    while item == exclude:
        item = random.choice(data)
    return item

def print_game_info(data_A, data_B, score=0, increaseScore=False):
    print(logo)
    if increaseScore:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}\n")
    print(vs)
    print(f"Compare B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}")

def get_user_choice():
    choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    while choice not in ['a', 'b']:
        choice = input("Invalid Input. Please try again.\nWho has more followers? Type 'A' or 'B': ").strip().lower()
    return choice

def compare_followers(data_A, data_B, user_choice):
    follower_count_A = data_A['follower_count']
    follower_count_B = data_B['follower_count']

    is_correct = (user_choice == 'a' and follower_count_A > follower_count_B) or (user_choice == 'b' and follower_count_B > follower_count_A)

    if is_correct:
        score = 1
        data_A = data_B
        data_B = get_random_data(exclude=data_A)
    else:
        score = 0

    return is_correct, data_A, data_B, score

def play_higher_lower():
    data_A = get_random_data()
    data_B = get_random_data(exclude=data_A)
    score = 0
    continue_game = True

    print_game_info(data_A, data_B)

    while continue_game:
        user_choice = get_user_choice()
        is_correct, data_A, data_B, round_score = compare_followers(data_A, data_B, user_choice)
        score += round_score
        os.system('clear')
        print_game_info(data_A, data_B, score, increaseScore=is_correct)
        continue_game = is_correct

    os.system('clear')
    print(logo)
    print(f"Sorry, that's wrong. Your final score: {score}")

play_higher_lower()
```
