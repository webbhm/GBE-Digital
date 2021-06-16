'''
Builds an image for the menu

Author: Howard Webb
Date: 2/16/2021
'''

from PIL import Image, ImageDraw, ImageFont
from variables import height, width, WHITE, BLACK, GRAY, fnt

def display_menu(menu):
    sleep_time = 0.05
    repeat_flag = False
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
        
    #convert menu to frame (via draw object)
    if menu is None:
       return
    #print(menu, "\n")
    count = 0
    row = 20
    selection = menu["selection"]
    # clear screen
    draw.rectangle((0, 0, width, height), outline=0, fill=WHITE)
    # Draw title box       
    draw.rectangle((10, row, width, row + 30), outline=0, fill=BLACK)
    draw.text((10, row), menu["name"], font=fnt, fill=WHITE)
    #print("Menu", menu["name"], len(menu["menu"]))
    count = 0
    for m in menu["menu"]:
        row += 30
        if count == selection:
            # Draw selected item
            #print("  *Item:", m["name"])
            draw.rectangle((0, row+1, width, row + 33), outline=0, fill=GRAY)
            draw.text((20, row), m["name"], font=fnt, fill=WHITE)    
        else:
            # Draw other items in menu
            #print("  Item:", m["name"])
            draw.text((20, row), m["name"], font=fnt, fill=BLACK)    
        count += 1
        
    return image, sleep_time, repeat_flag

    
    