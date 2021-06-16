'''
Configuration of experiemnt lights
An experiment has one or more phases - period of time with consistent lighting
Each phase has an on and off command (called via cron)
  the cmd is passed to the socket to change the lights
  depending on the handler, this could be a simple setting or dynamic
  
Author: Howard Webb
Date: 3/2/2021
'''
experiments = {
"Exp 1 High":{
    'name': 'Exp 1',
    'start_date': None,    
    'current_phase': 0,
    'phase_change':[],
    'phases': [
        {'name': "High", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}}]},

"Exp 1 Med":{
    'name': 'Exp 1',
    'start_date': None,        
    'current_phase': 0,
    'phase_change':[],    
    'phases': [
        {'name': "Medium", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}}]},

"Exp 1 Low":{
    'name': 'Exp 1',
    'start_date': None,        
    'current_phase': 0,
    'phase_change':[],    
    'phases': [
        {'name': "Low", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}}]},

"Exp 2":{
    'name': 'Exp 2',
    'start_date': None,        
    'current_phase': 0,
    'phase_change':[15],    
    'phases': [
        {'name': "Week 1-2", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}},
        {'name': "Week 3-4", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}}
        
        ]},
"Exp 3":{
    'name': 'Exp 3',
    'start_date': None,        
    'current_phase': 0,
    'phase_change':[15],        
    'phases': [
        {'name': "Week 1-2", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}},
        {'name': "Week 3-4", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}}
        
        ]},

"Exp 4":{
    'name': 'Exp 4',
    'start_date': None,        
    'current_phase': 0,
    'phase_change':[15],        
    'phases': [
        {'name': "Week 1-2", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}},
        {'name': "Week 3-4", 'start_date': None, 'lights': {
            'on': {
                'cmd': 'LIGHT_ON',
                'time': "8:00",
                'setting': {"R":75, "G":75, "B":75, "W":75}
                },
            'off': {
                'cmd': 'LIGHT_OFF',
                'time': "20:00",
                'setting': {"R":100, "G":100, "B":100, "W":100}
        }}}
        
        ]}
}

if __name__ == "__main__":
    print(experiments)