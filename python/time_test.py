import os
from datetime import datetime
from time import time
hr = 3
mn = 6
yr = 2021
m = 2
dy = 19
d = datetime(yr, m, dy)
print("Date", d)
print("Timestamp", d.timestamp())
t = d.timetuple()
d2 = datetime(t[0], t[1], t[2], hr, mn)
print("Date Time", d2)
print("Timestamp", d2.timestamp())

d3 = datetime.now()
t3 = d3.timetuple()
d3 = datetime(t[0], t[1], t[2], hr, mn)
print( d3)
ts3 = d3.timestamp()
print(ts3)

module_name = 'BME280_Proxy'
mod = 'BME280'
modul = __import__(module_name)
print("Type module:", type(modul))
#print("Attr", getattr(modul, _temperature))
class_ = getattr(modul, mod)
print("Class", class_)
instance = class_()
print("Type class", type(class_))
t, p, h = instance.getData()
print(t, p, h)
