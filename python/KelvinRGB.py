"""
    Based on: http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
    Comments resceived: https://gist.github.com/petrklus/b1f427accdf7438606a6
    Original pseudo code:
    
    Set Temperature = Temperature \ 100
    
    Calculate Red:
    If Temperature <= 66 Then
        Red = 255
    Else
        Red = Temperature - 60
        Red = 329.698727446 * (Red ^ -0.1332047592)
        If Red < 0 Then Red = 0
        If Red > 255 Then Red = 255
    End If
    
    Calculate Green:
    If Temperature <= 66 Then
        Green = Temperature
        Green = 99.4708025861 * Ln(Green) - 161.1195681661
        If Green < 0 Then Green = 0
        If Green > 255 Then Green = 255
    Else
        Green = Temperature - 60
        Green = 288.1221695283 * (Green ^ -0.0755148492)
        If Green < 0 Then Green = 0
        If Green > 255 Then Green = 255
    End If
    
    Calculate Blue:
    If Temperature >= 66 Then
        Blue = 255
    Else
        If Temperature <= 19 Then
            Blue = 0
        Else
            Blue = Temperature - 10
            Blue = 138.5177312231 * Ln(Blue) - 305.0447927307
            If Blue < 0 Then Blue = 0
            If Blue > 255 Then Blue = 255
        End If
    End If
"""

import math
from time import sleep
from PWM_Util import map

OFF = 100

class Kelvin(object):
    def __init__(self, light):
        self._light = light
        self.run()
        
    def run(self):
        low = 1000
        high = 40000
        step_size = 100
        for t in range(0, 15000, step_size):
            r, g, b = convert_K_to_RGB(t)
            r = round(map(r, 0, 256, OFF, self._light.R_MAX), 1)
            g = round(map(g, 0, 256, OFF, self._light.G_MAX), 1)
            b = round(map(b, 0, 256, OFF, self._light.B_MAX), 1)
            self._light.set_lights(r, g, b)
            sleep(0.25)
        self._light.off()            
            

def convert_K_to_RGB(colour_temperature):
    """
    Converts from K to RGB, algorithm courtesy of 
    http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
    """
    #range check
    if colour_temperature < 1000: 
        colour_temperature = 1000
    elif colour_temperature > 40000:
        colour_temperature = 40000
    
    tmp_internal = colour_temperature / 100.0
    
    # red 
    if tmp_internal <= 66:
        red = 255
    else:
        tmp_red = 329.698727446 * math.pow(tmp_internal - 60, -0.1332047592)
        if tmp_red < 0:
            red = 0
        elif tmp_red > 255:
            red = 255
        else:
            red = tmp_red
    
    # green
    if tmp_internal <=66:
        tmp_green = 99.4708025861 * math.log(tmp_internal) - 161.1195681661
        if tmp_green < 0:
            green = 0
        elif tmp_green > 255:
            green = 255
        else:
            green = tmp_green
    else:
        tmp_green = 288.1221695283 * math.pow(tmp_internal - 60, -0.0755148492)
        if tmp_green < 0:
            green = 0
        elif tmp_green > 255:
            green = 255
        else:
            green = tmp_green
    
    # blue
    if tmp_internal >=66:
        blue = 255
    elif tmp_internal <= 19:
        blue = 0
    else:
        tmp_blue = 138.5177312231 * math.log(tmp_internal - 10) - 305.0447927307
        if tmp_blue < 0:
            blue = 0
        elif tmp_blue > 255:
            blue = 255
        else:
            blue = tmp_blue
    
    return red, green, blue
    
      
def test():
    from GrowLight import GrowLight
    gl = GrowLight()
    k = Kelvin(gl)

if __name__ == "__main__":
    test()