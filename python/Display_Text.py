'''
Simple text display
This is a test case

Author: Howard Webb
Date: 2/21/2021
'''

from Display_Class import DisplayClass

# Display columns to load
_column_list = [{"module":"Column_Text", "class":"TextColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Test", "Text Column"]}               ]
_title = "Text Test"

class DisplayText(DisplayClass):
    pass
    