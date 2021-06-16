from exp import exp
from Exp_Util import save
from Client import SocketClient
from Display_Class import DisplayClass

_column_list = []

demo={'name': 'Sunrise', 'current_phase': 0, 'phases': [{'name':None, 'start_date': None, 'lights': {
    'on': {"cmd":"LIGHT_SUNRISE", 'time': None, "function":{"module":"Light_Custom", "class":"Sunrise"}},
    'off': {"cmd":"LIGHT_SUNSET",'time':None, "function":{"module":"Light_Custom", "class":"Sunset"}}
    }}                                                      
   ], 'plot': ([1, 2, 3], [4, 5, 6])}


class SunriseDemo(object):
    
    def __init__(self, title, column_list):
        self._socket = SocketClient()
        print("init SunriseDemo")
        # launch - move light controls to exp
        exp_hold = exp
        save(demo)
        # Call Client_Helper and pass command
        self.run()
        # restore last exp
        save(exp_hold)
        
    def receive(self, action):
        # dummy
        pass
        
        
    def run(self):
        print("run")
        message = demo["phases"][demo["current_phase"]]["lights"]["on"]["cmd"]
        self.send(message)
        message = demo["phases"][demo["current_phase"]]["lights"]["off"]["cmd"]
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
    
    
    