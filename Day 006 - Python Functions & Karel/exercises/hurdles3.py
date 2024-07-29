##Used in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right() 
    move()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    if front_is_clear():
        move()