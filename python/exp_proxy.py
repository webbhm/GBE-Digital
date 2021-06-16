exp={'name': 'Custom', 'current_phase': 0, 'phases': ["name":"Week 1+2", {'start_date': None, 'lights': {
    'on': {"cmd":"LIGHT_ON", 'time': '4:34', 'setting': {'R': 45, 'G': 56, 'B': 67, 'W': 78}},
    'off': {"cmd":"LIGHT_OFF",'time': None, 'setting': {'R': 100, 'G': 100, 'B': 100, 'W': 100}},
    }},
                                                      {"name":"Week 3+4", 'start_date': None, 'lights': {
    'on': {"cmd":"LIGHT_SUNRISE", 'time': '4:34', "function":{"module":"Lighting_Custom", "class":"Sunrise"}},
    'off': {"cmd":"LIGHT_SUNSET",'time':None, "function":{"module":"Lighting_Custom", "class":"Sunset"}}
    }},
{"name":"Week 5+6", 'start_date': None, 'lights': {
    'on': {"cmd":"LIGHT_CUSTOM_1", 'time': None, 'setting': {'R': 50, 'G': 50, 'B': 50, 'W': 50}},
    'off': {"cmd":"LIGHT_CUSTOM_2", 'time': None, 'setting': {'R': 100, 'G': 100, 'B': 90, 'W': 100}}    
    }}                                                      
   ], 'plot': ([1, 2, 3], [4, 5, 6])}
