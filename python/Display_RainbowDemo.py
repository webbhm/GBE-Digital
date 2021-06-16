'''
Run demo from menu
This file is the template for other light demos

Author: Howard Webb
Date: 2/8/2021
'''

from Client import SocketClient
from variables import UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT

_column_list = []

class RainbowDemo(object):
    
    def __init__(self, title, column_list):
        # ignore arguments, they are here for consistency of other displays
        self._socket = SocketClient()
        print("init Rainbow Demo")
        # launch - move light controls to exp
        
    def receive(self, action):
        # on receiving action run stuff
        self.run()
        return None, None, LEFT
        
    def run(self):
        # custom to the demo
        message = "LIGHT_RAINBOW"
        self.send(message)
        message = "LIGHT_OFF"
        self.send(message)
        
    def send(self, message):
        #cmd = {"cmd":message}
        #print("Send", message, {"cmd":message})
        response = self._socket.transmit(message)
        print("Resp:", response)
        
def test():
    print("Test Demo")
    d = RainbowDemo(None, None)
    
if __name__ == "__main__":
    test()
    
    
    