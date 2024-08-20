# Turtle Crossing Game

## Day 23 of 100 Days of Code - Python

### Overview

The Turtle Crossing game is a fun and interactive game built using Python and the `turtle` module. The player controls a turtle that needs to cross a road filled with moving cars without getting hit. The game becomes increasingly challenging as the cars speed up and the intervals between their appearances decrease.

### Project Details

For Day 23 of the 100 Days of Code challenge, I decided to take on the Turtle Crossing capstone project in the most challenging way possible. I chose to only look at the first step of the provided instructions and complete the rest on my own. This approach allowed me to dive deeper into the logic and structure of the game, ultimately leading to a more robust understanding of the concepts involved.

### Key Features

- **Car Class:** I implemented a `Car` class to handle the creation and movement of individual cars. This class was responsible for managing the appearance, movement, and speed of each car.

- **Car Manager Class:** The `CarManager` class was used to manage a collection of cars, creating new cars at random intervals and removing cars that moved off the screen. This class also handled communication between all cars and managed their collective behavior.

- **Collision Detection:** With the help of ChatGPT, I implemented collision detection between the player (turtle) and the cars. If a collision is detected, the game ends, signaling that the player has lost.

- **Removing Off-Screen Cars:** Another challenge I faced was removing cars that moved off the screen without affecting the cars still in play. I successfully implemented this feature with guidance from ChatGPT.

### Lessons Learned

- **Breaking Down the Problem:** This project was a constant reminder to break down complex problems into simpler, more manageable parts. By focusing on one aspect of the game at a time, I was able to build a functioning and enjoyable game.

- **Using External Resources:** While I tried to complete the project on my own, I found it beneficial to consult external resources like Stack Overflow, the turtle documentation, and ChatGPT when I encountered challenges.

- **Importance of Classes:** The use of classes like `Car` and `CarManager` made the code more modular and easier to manage, highlighting the importance of object-oriented programming principles in game development.

### Conclusion

Completing the Turtle Crossing game was a rewarding experience that reinforced my problem-solving skills and understanding of Python. It was a great reminder of the importance of breaking down complex problems, leveraging external resources, and staying persistent when facing challenges.

### How to Run the Game

To play the Turtle Crossing game:

1. Clone the repository.
2. Run `main.py`.
3. Use the `Up` arrow key to move the turtle upwards.
4. Avoid the cars and try to reach the other side of the road to score points.

Enjoy the game!

### Future Improvements

- Add different levels with increasing difficulty.
- Implement a scoring system based on time or the number of successful crossings.
- Add sound effects and animations for a more engaging experience.
