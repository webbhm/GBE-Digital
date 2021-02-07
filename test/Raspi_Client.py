import socket
from time import sleep
#from client_sensordata import GetTemp
#from monitor_client import transmit

sleepTime = 20
host = '127.0.0.1'
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
        s.send(str.encode(message))
        print("Message transmitted")
        reply = s.recv(1024)
        print("We have received a reply.")
        print("Send closing message.")
        s.send(str.encode("EXIT"))
        s.close()
        reply = reply.decode('utf-8')
        return reply

    def transmit(self, message):
        s = self.setupSocket()
        response = self.sendReceive(s, message)
        return response
    
class LightControl():
    
    def __init__(self):
        self.s = SocketClient()
        
    def lightOn(self):
    # turn the lights on
        message = "LIGHT_ON:"
        print("Transmitting Data.")
        response = self.s.transmit(message)
        print(response)

    def lightOff(self):
        # turn the lights off
        message = "LIGHT_ON:"
        print("Transmitting Data.")
        response = self.s.transmit(message)
        print(response)
    
    def lightSet(self, r, g, b, w):
        # set the LED pannel to specific values
        message = ("LIGHT_SET: {:d}: {:d}: {:d}: {:d}").format(r, g, b, w)
        print("Transmitting Data.")
        response = self.s.transmit(message)
        print(response)        
    
def test():
    s = SocketClient()
    message = "GET_TEMP:"
    while True:
        print("Transmitting Data.")
        response = s.transmit(message)
        print(response)    
        sleep(sleepTime)    

def testOn():
    s = SocketClient()
    message = "LIGHT_ON:"
    print("Transmitting Data:", message)
    response = s.transmit(message)
    print(response)    
    print("Done")

def testOff():
    s = SocketClient()
    message = "LIGHT_OFF:"
    print("Transmitting Data:", message)
    response = s.transmit(message)
    print(response)    
    print("Done")
    
def testSet():
    s = SocketClient()
    message = "LIGHT_SET: 55:77:80:40"
    print("Transmitting Data:", message)
    response = s.transmit(message)
    print(response)    
    print("Done")
    
if __name__ == "__main__":
    testOn()
    testOff()
    testSet()
    test()    