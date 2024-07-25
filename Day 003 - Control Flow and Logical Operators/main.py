print('''
*******************************************************************************
              .======.
              | INRI |
              |      |
              |      |
     .========'      '========.
     |   _      xxxx      _   |
     |  /_;-.__ / _\  _.-;_\  |
     |     `-._`'`_/'`.-'     |
     '========.`\   /`========'
              | |  / |
              |/-.(  |
              |\_._\ |
              | \ \`;|
              |  > |/|
              | / // |
              | |//  |
              | \(\  |
              |  ``  |
              |      |
              |      |
              |      |
              |      |
  \\jgs _  _\\| \//  |//_   _ \// _
 ^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ `^
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroad. Where do you want to go?:")
direction = input("    Type 'left' or 'right' \n")

if direction != "left":
  print("You fell into a hole. Game Over.")
  exit()


print("You've come to a lake. There is an island in the middle of the lake.")

swimOrBoat = input("    Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
if swimOrBoat != "wait":
  print("You get attacked by an angry trout. Game Over.")
  exit()

print("You arrive at the island unharmed. There is a house with 3 doors.")
door = input("    One red, one yellow and one blue. Which colour do you choose? \n")

if door == "red":
  print("It's a room full of fire. Game Over.")
elif door == "blue":
  print("You enter a room of beasts. Game Over.")
elif door == "yellow":
  print("You found the treasure! You Win!")
else: 
  print("You chose a door that doesn't exist. Game Over.")
  
exit()