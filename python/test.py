'''

t = (23, 45)
offset = 10
print(t)
t2 = (t[0] + offset, t[1] + offset)
print(t2)

R = 12
G = 45
B = 56
W = 78

foo = {"one":1, "two":2}
print(foo["one"])

env = {
    "name":None,
    "current_phase":None,
    "phases":[
        {"start_date":None,
         "lights":{
             "on":{"time":None, "setting":None},
             "off":{"time":None, "setting":None}}
             
         }
        ]}

on = {"time":None, "setting":{"R":R, "G":G, "B":B, "W":W}}
#print(env["phases"][0])
print(env["phases"],"\n")
print(env["phases"][0],"\n")
print(env["phases"][0]["lights"],"\n")
if "on" in env["phases"][0]["lights"]:
    env["phases"][0]["lights"]["on"] = on
else:
    env["phases"][0]["lights"] = {**env["phases"][0]["lights"], **light}
print(env["phases"][0]["lights"])

import Environ as e
e.makeENV()
e.set
'''
'''
import os
import glob
import shutil
# get name of thumb drive
f = glob.glob("/media/pi/*/")
print(f[0])
DIR = f[0]

target = DIR+"python"
if len(glob.glob(target)):
    # delete target directory
    shutil.rmtree(target)
shutil.copytree("/home/pi/python", target)
print("Copied")
'''
'''
try:
    shutil.copytree("/home/pi/python", f[0]+"python")
except Exception as e:
    print(e)
    if '[Errno 17]' == str(e)[0:10]:
        print("Hit")
'''
'''
from exp_test import exp
def cmd_dict(exp):
    cmd_dict = {}
    for k, v in exp["phases"][exp["current_phase"]]["lights"].items():
        print(k, v)
        cmd_line = {}
        setting = "setting"
        function = "function"
        if setting in v:
            cmd_line = {v["cmd"]:{"action":k, setting:v[setting]}}
        if function in v:
            cmd_line = {v["cmd"]:{"action":k, function:v[function]}}            
        cmd_dict = {**cmd_dict, **cmd_line}
    return cmd_dict

cmds = cmd_dict(exp)
print("Cmds")
print(cmds, '\n')
if "LIGHT_ON" in cmds:
    print("Found")
keys = []
for k, v in cmds.items():
    keys.append(k)
print("Keys", keys, '\n')
for key in keys:
    if "setting" in cmds[key]:
        print("S", cmds[key]["setting"])
    elif "function" in cmds[key]:
        print("F", cmds[key]["function"])

'''
'''
def foo():
    #return False
    pass

#x = False
x = foo()
print(x)
status = False

if status:
    print("True", status)
else:
    print("Status False")
'''

#print('{:2d}-{:2d}-20{:2d}'.format(3, 22, 21))

import datetime
from exp import exp

def dif_dates(date1,date2):
    return(abs(date2-date1).days)

def main():
    dt1 = exp["start_date"]
    reply = "Exp not started"    
    print(dt1)
    if dt1 is None:
        return reply
        d1 = dt1
    out = dt1.split('-')
    print(out[0], out[1], out[2][:2])
    yr = int(out[0])
    m = int(out[1])
    d = int(out[2][:2])
             
    d1 = datetime.date(yr, m, d)
    d2 = datetime.date.today()
    result1 = dif_dates(d2, d1)
    #reply = '{} days between {} and {}'.format(result1, d1, d2)
    reply = 'Exp Day: {}'.format(result1 + 1, d1, d2)
    return reply
    
reply = main()
print(reply)
    