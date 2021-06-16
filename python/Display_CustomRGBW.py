'''
Test of Display with Confirm
'''

from Display_Class import DisplayClass
from env import env
from Environ import set_lights

_column_list = [{"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"R", "column_first_line":32, "text_start_row": 80, "start_column":0, "end_column":59, "center":True, "low":1, "high":100},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"G", "column_first_line":32, "text_start_row": 80, "start_column":60, "end_column":119, "center":True, "low":0, "high":100},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"B", "column_first_line":32, "text_start_row": 80, "start_column":120, "end_column":179, "center":True, "low":0, "high":100},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"W", "column_first_line":32, "text_start_row": 80, "start_column":180, "end_column":240, "center":True, "low":0, "high":100},                
                     
                                                                                          # title, column_first_line,              text_start_row,       start_column,      end_column,       center,        low,     high
                {"module":"Column_SmallList", "class":"SmallListColumn", "exclude":True, "title":"Confirm", "column_first_line":32, "text_start_row": 80, "start_column":60, "end_column":130, "center":True, "text":["Yes", "No"]}                
               ]

class CustomRGBW(DisplayClass):
    def confirm(self, values):
        name = "Custom"
        R = values[0]
        G = values[1]
        B = values[2]
        W = values[3]
        set_lights(name, R, G, B, W)
        
