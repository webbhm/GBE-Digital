import I2C_LCD_driver
from time import sleep

menu = {}
max_lines = 2

class Menu:
   def __init__(self, addr, port=1):
       self.lcd = I2C_LCD_driver.lcd()
       self.home_menu = menu
       self.menu_depth = 0
       self.menu = menu[0]
       self.last_entry = 0

    def display_menu():
	self.lcd.display_string(self.menu, 1)
	self.lcd.display_string(self.menu[1], 2)
        self.last_entry = 1

    def menu_down():
        mylcd.lcd_clear()
	self.lcd.display_string(self.menu, 1)
        self.last_entry += 1
	self.lcd.display_string(self.menu[self.last_entry], 2)
	
    def menu_up():
        mylcd.lcd_clear()
	self.lcd.display_string(self.menu, 1)
        self.last_entry -= 1
	self.lcd.display_string(self.menu[self.last_entry], 2)

    def menu_select():
	if self.menu[self.last_entry].type == "Selection":
	    # execute function
            pass
        if self.menu[self.last_entry].type == "Menu"
            self.menu = menu[self.last_entry]
            self.menu_depth += 1
            self.display_menu()

    def menu_back():
        # walk to parent menu
        pass
        
	