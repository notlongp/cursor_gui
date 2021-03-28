import pyautogui
import math
import keyboard

def cursor_move_circular_motion(R=200):
    # getting the size of the screen
    (x, y) = pyautogui.size()

    # declaring the initial coordinates of the 
    # cursor to be in the middle of the screen
    (X, Y) = pyautogui.position(x/2, y/2)

    # tracker
    i = 0

    # nonstop loop
    while True:
        # cursor move every 6 degrees
        if i%6 == 0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
            if i%30 == 0:
                pyautogui.click(X, Y)
            i += 1
        else:
            i += 1

cursor_move_circular_motion()
        
