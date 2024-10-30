# Helping Reeborg the robot manoeuvre out of a fixed maze 

import random

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
def coin_toss():
    one_of_three = random.randint(0,3)
    if one_of_three == 0:
        turn_right()
    if one_of_three == 1:
        turn_left()
    if one_of_three == 2:
        turn_around()

while not at_goal():
    if not wall_in_front():
        move()
        if not wall_on_right():
            turn_right()
            if not wall_in_front():
                move()
        elif wall_on_right():
            turn_left()
            if not wall_in_front():
                move()
        else:
            turn_around()
            if not wall_in_front():
                move()            
    else:
        if not wall_on_right():
            turn_right()
            move()
        else:
            turn_left()
            if not wall_in_front():
                move()
            else:
                coin_toss()