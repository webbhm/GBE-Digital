import I2C_LCD_driver
from time import sleep


mylcd = I2C_LCD_driver.lcd()

def Hello_World():
    while True:
	mylcd.lcd_display_string("Hello World!", 2, 3)

def Hello_World_blink():
    while True:
        mylcd.lcd_display_string(u"Hello world!")
        time.sleep(1)
        mylcd.lcd_clear()
        sleep(1)

def Date():
    while True:
        mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    
        mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)
