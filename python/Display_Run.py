'''
Not a true display, but a stub for directly running applications from the menu
Designed for Light Demos
Generic classs customize by the config file and main_menu setup

Author: Howard Webb
Date: 2/28/2021
'''
from exp import exp
from Exp_Util import save
from Client import SocketClient
from variables import UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT

_sunrise_demo={'name': 'Sunrise', 'current_phase': 0, 'phases': [{'name':None, 'start_date': None, 'lights': {
    'on': {"cmd":"LIGHT_SUNRISE", 'time': None, "function":{"module":"Light_Custom", "class":"Sunrise"}},
    'off': {"cmd":"LIGHT_SUNSET",'time':None, "function":{"module":"Light_Custom", "class":"Sunset"}}
    }}                                                      
   ]}


class DisplayRun(object):
    
    def __init__(self, title, config):
        # override column list to use as function list
        self._socket = SocketClient()
        self._config = config
        print("init DisplayRun", title)
        exp_hold = exp
        save(self._config)
        # Call Client_Helper and pass command
        self.run()
        # restore last exp
        save(exp_hold)        
        
    def receive(self, action):
        # dummy
        return None, None, LEFT
        
        
    def run(self):
        # could be over-ridden for other actions
        print("run")
        message = self._config["phases"][self._config["current_phase"]]["lights"]["on"]["cmd"]
        self.send(message)
        message = self._config["phases"][self._config["current_phase"]]["lights"]["off"]["cmd"]
        self.send(message)
        
    def send(self, message):
        #cmd = {"cmd":message}
        #print("Send", message, {"cmd":message})
        response = self._socket.transmit(message)
        print("Resp:", response)
        
def test():
    print("Test Sunrise Demo")
    d = SunriseDemo(None, None)
    
if __name__ == "__main__":
    test()
    
    
    