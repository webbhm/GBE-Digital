'''
Client for interacting with the service (Grow Light)
Use the test function as a model for particular interaction functions

Author: Howard Webb
Date: 2/8/2021
'''

import socket
from time import sleep
import json


sleepTime = 20
host = '127.0.0.1' # localhost.  May be changed to make this an internet access
port = 5562

class SocketClient(object):
    
    def __init__(self):
        pass

    def setupSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.listen(5)
        except socket.error as msg:
            print(msg)
        print("Socket bind complete", host, port)
        #s.connect((host, port))
        return s

    def sendReceive(self, s, message):
        # convert dictionary to string/json
        s.send(str.encode(json.dumps(message)))
        print("Message transmitted")
        reply = s.recv(1024)
        print("We have received a reply.")
        print("Send closing message.")
        msg = json.dumps({"cmd":"EXIT"})
        s.send(str.encode(msg))
        s.close()
        reply = reply.decode('utf-8')
        return reply

    def transmit(self, message):
        s = self.setupSocket()
        response = self.sendReceive(s, message)
        return response
    
data_set = [{"cmd":"LIGHT_ON"}, {"cmd":"LIGHT_OFF"}, {"cmd":"LIGHT_SET", "args":{"R":45,"G":68, "B":77, "W":83}}, {"cmd":"Foo"}]       
    
def test():
    s = SocketClient()
    for message in data_set:
        print("Transmitting Data.")
        response = s.transmit(message)
        print(response)    
        sleep(sleepTime)    

if __name__ == "__main__":
    test()    