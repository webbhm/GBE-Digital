'''
Base class for columns
This is a simple text display
'''
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT
from Column_Class import ColumnClass

class TextColumn(ColumnClass):
    
    def __init__(self, draw, title, column_first_line, text_start_row, start_column, end_column, center, text):
        super().__init__(draw, title, column_first_line, text_start_row, start_column, end_column, center)
        self._text = text

    def get_active_body(self, action):
        # Simple multi-line display
        #print("Text - get_active_body")
        row = self._start_row
        for line in self._text:
            # start position of text
            start = HALF_CHAR
            if self._center_flag:
                # center the text
                pad = len(line)/2 * HALF_CHAR                
                start = self._center - pad
            #print(type(self._draw))
            #print(self._center, start, pad)
            self._draw.text((start, row), line, font=fnt, fill=BLACK)
            # increment for next row
            row += self._line_size

        
