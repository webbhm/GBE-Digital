'''
Joystick button initialization

Author: Howard Webb
Date: 2/16/2021
'''

import board
from digitalio import DigitalInOut, Direction

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

#print("A", board.D5)
#print("B", board.D6)
#print("L", board.D27)
#print("R", board.D23)
#print("U", board.D17)
#print("D", board.D22)
#print("C", board.D4)

#print("CS", board.CE0)
#print("DC", board.D25)
#print("Back", board.D26)
