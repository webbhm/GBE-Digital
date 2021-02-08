'''
Proxy class of GrowLight used for testin

Author: Howard Webb
Date: 2/8/2021
'''

from Light_Setting import *

OFF = 100

class GrowLight():
    
    def __init__(self):
        print("Init")
        self.R = args["setting"]["R"]
        self.G = args["setting"]["G"]
        self.B = args["setting"]["B"]
        self.W = args["setting"]["W"]
        self.on_func = args["on_func"]
        self.off_func = args["off_func"]
        # maximum safe settings
        self.R_MAX = 0
        self.G_MAX = 50
        self.B_MAX = 5
        self.W_MAX = 0        
        
        

    def set_lights(self, r, g, b, w=OFF):
             
        print(r, g, b, w)
        
    def on(self):
        print("On")
        
    def off(self):
        print("Off")
        
def test():
    gl = GrowLight()
    print("On")
    gl.on_func(gl)
    print("Off")
    gl.off_func(gl)
    print("Set Lights")
    gl.set_lights(45,56,67,78)
        
if __name__ == "__main__":
    test()
        
        