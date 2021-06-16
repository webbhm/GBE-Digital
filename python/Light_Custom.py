'''
Classes for dynamic custom light control
in main_menu set:
 module = "Light_Custom"
 class = name of one of these classes
 
Author: Howard Webb
Date: 2/27/2021
'''
        
class Sunrise(object):
    # create sunrise
    def __init__(self, light):
        import Sun 
        self._light = light
        Sun.sunrise(self._light)

class Sunset(object):
    # create sunrise
    def __init__(self, light):
        import Sun 
        self._light = light
        Sun.sunset(self._light)
        
class Rainbow(object):        
    # create rainbow
    def __init__(self, light):
        from Rainbow import Rainbow as R 
        self._light = light
        R(self._light)

class Kelvin(object):
    # create temperature spectrum
    def __init__(self, light):
        from KelvinRGB import Kelvin as K 
        self._light = light
        K(self._light)

