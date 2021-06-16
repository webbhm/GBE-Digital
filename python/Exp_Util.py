'''
Create and manage Exp.py file
# Build dictionary structure of variables for an experiment
# A python file is generated that is 'read' by other programs
# Author: Howard Webb
# Data: 2/21/2018
'''

import uuid
import json
from datetime import datetime
import os

DIR = "/home/pi/python/"
file_nm = "exp.py"
file_path = DIR + file_nm

EXP_MISMATCH = 2
PHASE_MISMATCH = 3
PHASE_CONFIRM = 4

def makeExp():
    exp={
        "name":None,
        "current_phase":0,
        "phases":[
            {"start_date":None,
             "lights":{
                 "on":{"time":None, "setting":None},
                 "off":{"time":None, "setting":None}
                 }
             }
            ]}
    
    saveDict('exp', file_path, exp)
    
def Trials():
    trials = []
    timestamp = datetime.utcnow().isoformat()[:19]
    id = str(uuid.uuid4())
    trials = [{'id':id, 'start_date':timestamp}]
    return trials

def set_lights(exp_name, light_name, R, G, B, W):
    # set light setting
    # assumes this is custom, hence only one phase
    from exp import exp
    exp["name"] = exp_name

    light = {"time":None, "setting":{"R":R, "G":G, "B":B, "W":W}}
    if light_name in exp["phases"][0]["lights"]:
        exp["phases"][0]["lights"][light_name] = light
    else:
        exp["phases"][0]["lights"][light_name] = light
    saveDict('exp', file_path, exp)
    print("Confirm:", exp_name, R, G, B, W)

def set_on(time):
    from exp import exp
    exp["phases"][0]["lights"]["on"]["time"] = time
    saveDict('exp', file_path, exp)
    print("Confirm:",time)

def set_off(time):
    from exp import exp
    exp["phases"][0]["lights"]["off"]["time"] = time
    saveDict('exp', file_path, exp)
    print("Confirm:", time)

def set_start_date(date):
    # set start date of the experiment
    from exp import exp
    exp["start_date"] = date
    saveDict('exp', file_path, exp)
    print("Confirm:", date)

def set_plot(values):
    print("Set Plot", values)
    from exp import exp
    exp["plot"] = values
    saveDict('exp', file_path, exp)
    #print("Plot Saved")

def prettyPrint(txt):
    '''Dump json in nice format'''
    #print type(txt)
    print(json.dumps(txt, indent=4, sort_keys=True), '\n')

def saveDict(name, file_name, conf_dict):
    #print(values)
    f = open(file_name, 'w+')
    tmp=name+'='+str(conf_dict)
    f.write(tmp)
    f.close()
    
def save(conf_dict):
    print("Exp_Util save")
    saveDict('exp', file_path, conf_dict)
    
def set_phase(name, phase):
    # Advance an experiment to the next phase
    from exp import exp
    print('\n', "Set Phase", exp["name"], name, exp["current_phase"], phase, '\n')
    if exp["name"] != name:
        print("Exp mis-match", exp["name"], name)
        return EXP_MISMATCH
    elif exp["current_phase"] != phase - 1:
        print("Phase error", exp["current_phase"], phase)
        return PHASE_MISMATCH
    
    exp["current_phase"] = phase
    timestamp = datetime.utcnow().isoformat()[:19]    
    exp["phases"][exp["current_phase"]]["start_date"] = timestamp
    save(exp)
    
def update():
    # save changes to env
    save(env)
    
    
def test():
    makeExp()
    from exp import exp
    prettyPrint(exp)
    set_lights("Custom", "on", 45, 56, 67, 78)
    from exp import exp
    prettyPrint(exp)
    set_on("4:34")
    from exp import exp
    prettyPrint(exp)
    set_plot(([1,2,3],[4,5,6]))
    from exp import exp
    prettyPrint(exp)    

if __name__=="__main__":
    test()
    
    
    


    
