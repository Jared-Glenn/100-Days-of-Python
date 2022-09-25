'''
Reeborg's World Puzzle

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

first_loop = 0

while not at_goal():
    if right_is_clear() and first_loop <= 2:
        turn_right()
        move()
        if is_facing_north():
            first_loop += 1
    elif front_is_clear() and first_loop <= 1:
        move()
    else:
        turn_left()
        first_loop = 0