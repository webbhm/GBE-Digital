'''
Base class for columns
Builds title but blank column
'''
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT

class ColumnClass(object):
    
    def __init__(self, draw, title, column_first_line, text_start_row, start_column, end_column, center):
        #print("init ColumnClass")
        self._title = title
        self._draw = draw
        self._line_size = 30
        self._start_row = text_start_row
        #print(self._start_row)
        self._column_first_line = column_first_line
        self._start_column = start_column
        self._end_column = end_column
        self._center = self._start_column + (self._end_column - self._start_column)/2
        #print("center", self._center, self._start_column, self._end_column)
        self._column_width = self._end_column - self._start_column # width of column
        self._title_half = 0
        if self._title is not None:
            self._title_half =self._center - len(self._title)/2 * HALF_CHAR  # padding for title display
        self._center_flag = center  # flag for centering text
        self._title_start = self._start_column
        if self._title is not None and self._center_flag:
            self._title_start =self._center - len(self._title)/2 * HALF_CHAR  # padding for title display
            
        self._selection = None
        #self.get_image()
        #print("Column_Class: init Finished")
        
    # Screen creation functions
        
    def get_image(self, action):
        self.get_active_image(action)
        
    def get_active_image(self, action):
        self.get_title(action)
        self.clear_column()
        self.get_active_body(action)
        
    def get_static_image(self, action):
        self.get_title(action)
        self.clear_column()
        self.get_static_body(action)

    def clear_column(self):
        #print("Clear Column")
        rect = self.get_column_rectangle()
        self._draw.rectangle(rect, outline=WHITE, fill=WHITE)
        
    def get_column_rectangle(self):
        upper_right = self._column_first_line + self._line_size
        if self._title is None:
            upper_right = self._column_first_line
        return (self._start_column, upper_right, self._end_column, height)
        
    def get_title(self, action):
        # Title Frame
        # color title
        #print("Col Title", self._title, (self._title_start, self._column_first_line))
        #self._draw.rectangle((self._start_column, self._column_first_line, self._end_column, height), outline=WHITE, fill=(0, 0, 200))
        # Draw title
        if self._title is None:
            self._start_row = self._column_first_line
            return
        self._draw.text((self._title_start, self._column_first_line), self._title, font=fnt, fill=BLACK)

    def get_active_body(self, action):
        #print("Default active body")
        pass

    def get_static_body(self, action):
        #print("Default static body")
        # Simple multi-line display
        pass

    # action handlers below here

    def init(self, action):
        # special action for new instance
        #print("Default Column INIT")
        self.get_image(action)
        return None, None, None
    
    def loop(self, action):
        # ScreenManager loop with nothing pressed
        # Default - no action
        return None, None, None

    def left(self, action):
        # move back handled by display
        # Default - no action        
        return None, None, None
        
    def right(self, action):
        # Default - no action        
        return None, None, None
    
    def up(self, action):
        #print(type(self._active_wheel))
        # Default - no action        
        return None, None, None
        
    def down(self, action):
        #print(type(self._active_wheel))
        # Default - no action        
        return None, None, None
        
    def center(self, action):
        # Default - no action        
        return None, None, None
        
    def receive(self, action):
        # handles incoming actions 
        if action == INIT:
            return self.init(action)
        if action == LOOP:
            return self.loop(action)
        elif action == LEFT:
            return self.left(action)
        elif action == RIGHT:
            return self.right(action)
        elif action == UP:
            return self.up(action)
        elif action == DOWN:
            return self.down(action)
        elif action == CENTER:
            return self.center(action)
        else:
            return None, None, None
        
        
        
