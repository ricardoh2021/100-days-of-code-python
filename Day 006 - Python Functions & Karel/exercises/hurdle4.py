#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def clear_hurdle():
    turn_right()
    move()
    turn_right() 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    print(wall_on_right())
    if wall_in_front() and right_is_clear():
        clear_hurdle()
    elif wall_in_front():
        turn_left()
    elif front_is_clear() and right_is_clear() and is_facing_north():
        clear_hurdle()
    else:
        move()
        
        