_column_list = []

import os

class TurnLightsOn(object):
    
    def __init__(self, title, column_list):
        os.system('python3 /home/pi/python/Light_Switch.py -a on')
        
    def receive(self, action):
        pass
        
class TurnLightsOff(object):
    
    def __init__(self, title, column_list):
        os.system('python3 /home/pi/python/Light_Switch.py -a off')
        
    def receive(self, action):
        pass        
       
def test():
    print("Test Light Switch")
    print("On")
    d = TurnLightsOn(None, None)
    print("Off")
    d = TurnLightsOff(None, None)
    print("Done")
    
if __name__ == "__main__":
    test()
    
    
    