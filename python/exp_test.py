exp={'name': 'Custom', 'current_phase': 0, 'phases': [{'name':'Week 1+2', 'start_date': None, 'lights': {
    'on': {"cmd":"LIGHT_ON", 'time': '4:34', 'setting': {'R': 45, 'G': 56, 'B': 67, 'W': 78}},
    'off': {"cmd":"LIGHT_OFF",'time': None, 'setting': {'R': 100, 'G': 100, 'B': 100, 'W': 100}},
    'foo': {"cmd":"LIGHT_SUNRISE", 'time': '4:34', "function":{"module":"Light_Custom", "class":"Sunrise"}},
    'xyz': {"cmd":"LIGHT_SUNSET",'time':None, "function":{"module":"Light_Custom", "class":"Sunset"}},
    'abc': {"cmd":"LIGHT_CUSTOM", 'time': None, 'setting': {'R': 50, 'G': 50, 'B': 50, 'W': 50}},
    'zzz': {"cmd":"LIGHT_CUSTOM_2", 'time': None, 'setting': {'R': 100, 'G': 100, 'B': 90, 'W': 100}},
    'cam': {"cmd":"LIGHT_CAMERA"}        
    }}                                                      
   ], 'plot': ([1, 2, 3], [4, 5, 6])}
