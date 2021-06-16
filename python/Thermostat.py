'''
Thermostat to check temperature and adjust fan

Author: Howard Webb
Date: 3/14/2021

'''
from BME280 import BME280
from Fan import Fan


class Thermostat(object):
    
    def __init__(self):
        self._temp = BME280()._temp
        self._fan = Fan()
        speed = self._fan.adjust(self._temp)
        print("Temp", self._temp, "Speed", speed)
        
def main():
    t = Thermostat()
    
if __name__ == "__main__":
    main()