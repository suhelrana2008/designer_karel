from karel.stanfordkarel import *

"""
Karel will design the world with beepers.
"""

def main():
    complete_row()
    back_home()
    finish_till_end()
    turn_right()
    while front_is_clear():
        move()
    
# Creating this function to complete the row
def complete_row():        
    while front_is_clear():
        beepers_till_end()
    put_beeper()

# This function will fill the beepers in a row
def beepers_till_end():
    if front_is_clear():
        put_beeper()
        move()

# This function will help Karel avoid hitting the wall.        
def finish_till_end():    
    while right_is_clear():
        step_up()
        back_home()
    go_to_end()
    
# This function will help Karel to move upward and avoid hitting the wall
def step_up():
    turn_right()
    move()
    if front_is_clear():
        move()
        turn_right()
        complete_row()

# It will help Karel to finish the game with facing east.    
def go_to_end():
    turn_left()
    turn_left()
    while front_is_clear():
        move()

# When Karel finish 1 row, it'll help to go up and finish next row with beepers    
def next_row():    
    turn_right()
    if front_is_clear():
        move()
        turn_right()
        move()
    complete_row()  
    
# After completing a row Karel needs to back home for next mission        
def back_home():
    turn_left()
    turn_left()
    while front_is_clear():
        move()

# used for loop for 3 times turn_left        
def turn_right():
    for i in range(3):
        turn_left()
        

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()