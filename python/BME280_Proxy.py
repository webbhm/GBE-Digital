'''
Proxy object for the BME280
'''
import time

import random

class BME280(object):
        
    def getData(self):
        # temperature
        tr = random.randint(180, 300)
        t = round((tr/10), 1)
        # pressure
        pr = random.randint(280, 310)
        p = round((pr/10), 1)
        # humidity
        hr = random.randint(200, 500)
        h = round((hr/10), 1)

        return t, p, h
    
    
def test():
    bme = BME280()
    for x in range(0, 20):
      temperature,pressure,humidity = bme.getData()
      #adj_bar = bme.adj_baro(pressure, temperature)
      #print("Adj {}".format(bme.adj_baro(pressure, temperature)))

      print( "Temperature: {}C".format(temperature))
      print( "Pressure: {}hpa, {}In".format(pressure, round(pressure * 0.02953, 2)))
      print( "{}: {}%".format("Humidity", humidity))
      time.sleep(3)
    print("Done")
    
    

if __name__=="__main__":
   test()
        