# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random 

headsOrTails = random.randint(0,1)

#Decided to use ternary operator to shorten this up.
result = "Heads" if headsOrTails == 1 else "Tails"

print(result)