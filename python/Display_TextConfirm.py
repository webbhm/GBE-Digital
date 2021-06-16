'''
Test of Display with Confirm
'''

from Display_Class import DisplayClass

_column_list = [{"module":"Column_Text", "class":"TextColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Test", "Text Column"]},
                {"module":"Column_SmallList", "class":"SmallListColumn", "exclude":True, "title":"Confirm", "column_first_line":32, "text_start_row": 80, "start_column":60, "end_column":240, "center":True, "text":["Yes", "No"]}                
               ]
_title = "Confirm Test"

class TextConfirm(DisplayClass):
    pass
