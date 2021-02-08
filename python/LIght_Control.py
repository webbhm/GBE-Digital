'''
High level object that coordinates the relatinship between the Light and the Socket service
Passes the light's command handler to the socket
Defines the light commands
Starts the service - this gets set-up via systemd, but may be run from a command prompt for development and testing
Use Client.py to communicate with the Service

Author: Howard Webb
Date: 2/8/2021
'''
from GrowLight_Proxy import GrowLight
from Server import Server
from CommandHandler import CommandControl

data_set = [{"cmd":"LIGHT_ON"}, {"cmd":"LIGHT_OFF"}, {"cmd":"LIGHT_SET", "args":{"R":45,"G":68, "B":77, "W":83}}, {"cmd":"Foo"}]       

class LightControl(object):
    
    def __init__(self):
        print("Initialize Light Control")
        self.light = GrowLight()
        self.server = Server(CommandControl(self.light))
        self.run()
        
    # Start the Server running
    def run(self):
        print("Run")
        while True:
            try:
                conn = self.server.setupConnection()
                self.server.dataTransfer(conn)
            except Exception as e:
                print(e)
                break
            
lc = LightControl()            
