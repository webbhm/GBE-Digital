"""
Vernier CO2 sensor - via Go Direct
Technical notes of commands and operation and from:
https://vernierst.github.io/godirect-examples/python/
Install with:
pip3 install godirect[USB,BLE]

 Author : Howard Webb
 Date   : 06/20/2018
 
"""

from gdx import gdx
from LogUtil import Logger
from time import sleep

class V_CO2(object):

    def __init__(self, logger=None):
        self._logger = logger
        if logger == None:
            self._logger = Logger("V_CO2", Logger.INFO)
        
        self._gdx = gdx()
        self._gdx.open_usb()
        #self._headers = self._gdx.enabled_sensor_info(self._gdx)
        self._headers = self._gdx.enabled_sensor_info()
        self._info = self._gdx.sensor_info()
        self._logger.info("Initialized V_CO2")
        sleep(20)  # wait 20 seconds to warm up
        
    def _exit_(self):
        self.close()
        
    def close(self):        
        self._gdx.stop()
        self._gdx.close()
        
       
    def info(self):
        # 0 = sensor number, 1 = description, 2 = units, 3 = incompatible sensors
        for info in self._info:
            sensor_number = info[0]
            sensor_description = info[1]  
            sensor_units = info[2]  
            incompatible_sensors = info[3]  
            print("sensor number = ", sensor_number)
            print("sensor description = ", sensor_description)
            print("sensor units = ", sensor_units)
            print("incompatible sensors = ", incompatible_sensors)
            print()
        print('End Sensor Info')            

    def read(self):
        self._gdx.select_sensors([1,2, 3])
        self._gdx.start(period=1000)
        for x in range(0, 6):
            data = self._gdx.read()
            print(data)
            
    def getData(self):
        self._gdx.select_sensors([1,2, 3])
        self._gdx.start(period=1000)
        data = self._gdx.read()
        if data is None:
            return None
        
        temp = data[0]
        humidity = data[1]
        co2 = data[2]
        return temp, humidity, co2
        
        
            
    def log(self):
        # isolate Sheet to this function
        # Note: this is a push data function 
        from G_AppendUtil import AppendUtil
        util = AppendUtil()
        # Pull data from all three channels co2, temp, humidity
        self._gdx.select_sensors([1,2,3])
        self._gdx.start(period=1000)
        while True:
            data = self._gdx.read()
            co2 = data[0]
            temp = data[1]
            hum = data[2]
            c_rec = ['Environment_Observation', '', 'Canopy', 'Air', 'CO2', "{:3.1f}".format(co2), 'ppm', 'Vernier', 'Success','']
            t_rec = ['Environment_Observation', '', 'Canopy', 'Air', 'Temperature', "{:3.1f}".format(temp), 'C', 'Vernier', 'Success','']
            h_rec = ['Environment_Observation', '', 'Canopy', 'Air', 'Humidity', "{:3.1f}".format(hum), '%', 'Vernier', 'Success','']
            util.save(c_rec)
            util.save(t_rec)
            util.save(h_rec)
            sleep(3)
            
            print(data)
            


def test(level=Logger.DEBUG):
    print("Test Vernier CO2")
    co2 = V_CO2()
    co2._logger.setLevel(level)
    if co2._headers != None:
        print('Headers')
        print(co2._headers)
        print('End Headers')
    co2.info()
    co2.read()
    print("Done")
    co2.close()
        
def validate():
    test(Logger.INFO)
    
    
def main():
    co2 = V_CO2()
    co2._logger.setLevel(Logger.INFO)
    co2.log()
    
def test2():
    co2 = V_CO2()
    while True:
        temp, humidity, co2 = co2.getData()
        print("Temperature: ", temp)
        print("Humidity: ", humidity)
        print("CO2: ", co2)
    

if __name__ == "__main__":
    test2()
