'''
Proxy for the Light_Controller and Client
Allows for testing of command handlers and simulates how the Light_Control works

Author: Howard Webb
Date: 2/8/2021
'''

from GrowLight_Proxy import GrowLight
from Server_Proxy import Server
from CommandHandler import CommandControl
import json

# Test set of command messages
data_set = [{"cmd":"LIGHT_ON"}, {"cmd":"LIGHT_OFF"}, {"cmd":"LIGHT_SET", "args":{"R":45,"G":68, "B":77, "W":83}}, {"cmd":"Foo"}]       

class LightControl(object):
    
    def __init__(self):
        print("Initialize Light Control")
        self.light = GrowLight()
        self.server = Server(CommandControl(self.light))
        self.run()
        
    def run(self):
        print("Run")
        try:
            for data in data_set:
                print(data)
                # convert dictionary/json to text
                text = json.dumps(data)
                reply = self.server.dataTransfer(text)
                print(reply)
        except Exception as e:
            print(e)
            
lc = LightControl()            
    
'''
while True:
    try:
        #conn = s.setupConnection()
        #s.dataTransfer(conn)
        for data in data_set:
            print(data)
            s.dataTransfer(data)
    except Exception as e:
        print(e)
        break
'''        