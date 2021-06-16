'''
Move the experiment descriptor to exp.py
        
Author: Howard Webb
Date: 2/22/2021
'''

from Display_Class import DisplayClass
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, LOOP, CENTER, INIT
#import exp_conf  # experiment configuration dictionary
from File_Util import copy, remove, get_drive

DRIVE_MISSING = 2
#PHASE_MISMATCH = 3
CONFIRM = 4

# column definitions referenced in main_menu

_column_list = [{"module":"Column_Text", "class":"TextColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Updated", "", ""]}]
              
class DisplayData(DisplayClass):
    
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        #self._confirm_flag = True
        self._reply_flag = True
        
        print("Text", len(self._text))
        self._home_dir = "/home/pi/"
        self._data_dir = "data"
        self._picture_dir = "Pictures"
        self._log_dir = "logs"
        self._file_name = "exp.py"
        
        self._drive = get_drive()
        txt1 = ""
        txt2 = ""
        txt3 = ""
        if self._drive == None:
            txt1 = "Insert Drive"
            txt2 = "Then Retry"
        elif self._title == "Import Data":
            txt1 = "Copy To"
            txt2 = "Thumb Drive"
        elif self._title == "Export Data":
            txt1 = "Copy To"
            txt2 = "Thumb Drive"
        elif self._title == "Delete Data":
            txt1 = "Delete Data"
            txt2 = "Pictures"
            txt3 = "Logs"
        # reset after changes    
        self._column_list[0]["text"] = [txt1, txt2, txt3]
        print("init", self._text)
        self._columns = []
        self.load_columns()
        
    def confirm(self, action):
        #
        action = None
        txt1 = ""
        txt2 = ""
        txt3 = ""
        self._drive = get_drive()
        if self._drive == None:
            # thumb drive not iserted
            txt1 = "Insert Drive"
            txt2 = "Then Retry"
            txt3 = ""
        if self._title == "Import Data":
            # undefined for now
            source = None
            target = None
            #copy(source, target)
            txt1 = "Data Moved"
            txt2 = "Thumb Drive"
        elif self._title == "Export Data":
            # export data, Pictures and exp.py
            self.export()
            txt1 = "Copied To"
            txt2 = "Thumb Drive"
        elif self._title == "Delete Data":
            # remove data
            target = self._drive + self._data_dir + "/*"
            self.remove(target)
            # remove pictures
            target = self._drive + self._picture_dir + "/*.jpg"
            self.remove(target)
            #remove lapse images
            target = self._drive + self._picture_dir + "/lapse/*.jpg"
            self.remove(target)
            
            txt1 = "Data Erased"
            
        self._reply_text = [txt1, txt2, txt3]            
        return CONFIRM
    
    def export(self):
        print("Move Data")
        source = self._home_dir + self._data_dir
        target = self._drive + self._data_dir
        copy(source, target)    
        print("Moved", source, target)
    
        print("Move Pictures")
        source = self._home_dir + self._picture_dir
        target = self._drive + self._picture_dir
        copy(source, target)
        print("Moved", source, target)
    
        print("Move Logs")
        source = self._home_dir + self._log_dir
        target = self._drive + self._log_dir
        copy(source, target)
        print("Moved", source, target)
        
        print("Move exp.py")
        self._file_name = "exp.py"
        source = self._home_dir + "python/" + self._file_name
        target = self._drive + self._file_name
        copy(source, target)
        print("Moved", source, target)
        
    
        
 


