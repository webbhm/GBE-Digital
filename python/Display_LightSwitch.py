'''
Objects to match menu pattery
used in menues

Author: Howard Webb
Date: 3/8/2021
'''

_column_list = []

import os
from variables import UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT

class LightSwitchOn(object):
    
    def __init__(self, title, column_list):
        os.system('python3 /home/pi/python/Light_Switch.py -a on')
        
    def receive(self, action):
        return None, None, LEFT
        
class LightSwitchOff(object):
    
    def __init__(self, title, column_list):
        os.system('python3 /home/pi/python/Light_Switch.py -a off')
        
    def receive(self, action):
        return None, None, LEFT       
       
def test():
    print("Test Light Switch")
    print("On")
    d = LightSwitchOn(None, None)
    print("Off")
    d = LightSwitchOff(None, None)
    print("Done")
    
if __name__ == "__main__":
    test()
    
    
    