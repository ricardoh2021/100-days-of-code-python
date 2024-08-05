# Blackjack Project Notes

## Overview

This project implements a simplified version of the Blackjack game in Python. The rules and game flow are designed to mimic the basic mechanics of the game.

## Key Features

- The deck is unlimited in size.
- No jokers included.
- Face cards (Jack, Queen, King) count as 10.
- Aces can count as either 11 or 1.
- Cards have equal probability of being drawn and are not removed from the deck after being drawn.
- The computer acts as the dealer.

## Optimization

I used ChatGPT to optimize my code. Here are some of the improvements:

- Defined constants for card values to enhance code readability.
- Combined conditions for dealer card dealing logic to simplify the code.
- Avoided redundant sum calculations by tracking the user's score directly as cards are added.
- Removed redundant function calls and simplified the flow of the game logic.

## Functions Documentation

### get_user_input(prompt)

Prompt the user for input and validate the response.

**Args:**

- `prompt (str)`: The prompt message to display.

**Returns:**

- `response (str)`: The validated user input, either 'y' or 'n'.

### deal_computer_cards()

Deal cards to the computer (dealer) until the sum is at least 17.

**Returns:**

- `dealer_cards (list)`: The list of cards dealt to the dealer.

### starting_user_hand()

Deal the initial two cards to the user.

**Returns:**

- `user_cards (list)`: The initial two cards dealt to the user.

### deal_user_card(user_cards)

Deal an additional card to the user.

**Args:**

- `user_cards (list)`: The current list of cards held by the user.

### print_final_scores(user_cards, dealer_cards, user_score, dealer_score)

Print the final scores of the user and the dealer.

**Args:**

- `user_cards (list)`: The list of cards held by the user.
- `dealer_cards (list)`: The list of cards held by the dealer.
- `user_score (int)`: The user's final score.
- `dealer_score (int)`: The dealer's final score.

### play_blackjack()

Play a single session of Blackjack.
