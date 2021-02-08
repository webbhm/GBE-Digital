'''
Test building of the menu dictionary and exercise walking through it
The functions (up, down, back, select) will be tied to buttons or a joystick

Author: Howard Webb
Date: 2/8/2021
'''

menu = {}
#build temperature menu
f_func =  {"name":"Farenheight", "function":"displayF"}
c_func = {"name":"Centegrade", "function":"displayC"}
t_menu = []
t_menu.append(f_func)
t_menu.append(c_func)
tmp_menu = {}
tmp_menu["name"] = "Temp Menu"
tmp_menu['menu'] = t_menu

# build time menu
tm_func = {"name":"Time", "function":"displayTime"}
d_menu = []
d_menu.append(tmp_menu)
d_menu.append(tm_func)

# build display menu (time & temp)
disp_menu = {}
disp_menu["name"] = "Display Menu"
disp_menu["menu"] = d_menu

# build experiment menu
e1_func = {"name":"Exp_1", "function":"setExp1"}
e2_func = {"name":"Exp_2", "function":"setExp2"}
e3_func = {"name":"Exp_3", "function":"setExp3"}
e4_func = {"name":"Exp_4", "function":"setExp4"}
e_menu = []
e_menu.append(e1_func)
e_menu.append(e2_func)
e_menu.append(e3_func)
e_menu.append(e4_func)
exp_menu = {}
exp_menu["name"] = "Experiment Menu"
exp_menu["menu"] = e_menu

d_func = {"name":"Diagnostics", "function":"validate"}
# build home menu (display and exp)
h_menu = []
h_menu.append(disp_menu)
h_menu.append(exp_menu)
h_menu.append(d_func)
home_menu = {}
home_menu["name"] = "Home Menu"
home_menu["menu"] = h_menu

menu = home_menu

print(menu)
'''
menu = {
    {"name":"Home Menu", 
        "menu":[ 
            {"name":"Display Menu", 
            "menu":[ 
                {"name":"Temp",  
                    "menu":[ 
                        {"name":"Farenheight", "function":"displayF"}, \
                        {"name":"Centegrade", "function":"displayC"} \
                           ] 
                 }, 
                {"name":"Time", "function":"displayTime"} \
                    ] 
            }, 
            {"name":"Experiment Menu", 
            "menu":[ 
                {"name":"Exp_1", "function":"setExp1"}, 
                {"name":"Exp_2", "function":"setExp2"}, 
                {"name":"Exp_3", "function":"setExp3"}, 
                {"name":"Exp_4", "function":"setExp4"} 
                    ] 
            } 
        ]}     
    }
'''    
stk = [] # stack to handle walking through layers
selection = 0 # selection scrolled to within a menu

def display():
    # Proxy for sending to a screen
    global selection
    global stk
    menu = stk[len(stk)-1]
    print("Menu:", menu["name"])
    count = 0
    for m in menu["menu"]:
        if count == selection:
            print("  *Item:", m["name"])
        else:
            print("  Item:", m["name"])
        count += 1

def back():
    # If in menu, back key returns to the previous menu
    # If working a function, it moves back to the last menu
    global selection
    # If in  menu, move up a level
    if 'menu' in stk[len(stk)-1]:    
    # Move up a menu level
        if len(stk) == 1: # already at top menu  
            return
        else:
            stk.pop()
            # get last saved selection
            selection = stk[len(stk)-1]['selection']
            #selection = 0
            display()
    elif 'function' in stk[len(stk)-1]:
        stk.pop()
        display()
        
def up():
    # Move up in selections
    global selection
    if selection == 0:
        return
    else:
        selection -= selection
        #print(stk[len(stk)-1][selection]['name'])
    display()
        
        
def down():
    # Move down in selections
    global stk
    global selection
    #print(selection, len(stk))
    #print(stk)
    #print(stk[len(stk)-1])
    if selection == len(stk[len(stk)-1]['menu'])-1:
        return
    else:
        selection += 1
        #print(len(stk)-1, selection)
        #print(stk[len(stk)-1])
        #print(stk[len(stk)-1]['menu'][selection]['name'])
    display()

def select():
    # Pick an item from the menu
    global selection

    
    if 'menu' in stk[len(stk)-1]['menu'][selection]:
        # save last selection for when return
        stk[len(stk)-1]['selection'] = selection
        stk.append(stk[len(stk)-1]['menu'][selection])
        selection = 0
        display()
    elif 'function' in stk[len(stk)-1]['menu'][selection]:
        stk.append(stk[len(stk)-1]['menu'][selection])
        print(stk[len(stk)-1])
        print("Run", stk[len(stk)-1]["name"])
        
def home():
    # Return to top menu
    global selection
    global stk
    stk = []
    stk.append(menu)
    selection = 0
    display()
        
# Test out the menu
stk.append(menu)
display()
#print(len(stk[len(stk)-1]['menu']), selection, '\n')
#print(stk[len(stk)-1]['menu'], '\n')
down()
print("Down\n")
#print(len(stk), selection, '\n')
#print(stk[len(stk)-1], '\n')
#print(stk[len(stk)-1]['menu'], '\n')
#print(stk[len(stk)-1]['menu'][selection], '\n')
print("Select", selection, '\n')
select()
#print(stk[len(stk)-1])
down()
print("Down\n")
down()
print("Down\n")
print("Select", selection, '\n')
select()
back()
print("Back\n")
back()
print("Back\n")
#print(len(stk)-1, selection, '\n')
#print("*", stk[len(stk)-1], '\n')
up()
print("Up\n")
#print(len(stk)-1, selection, '\n')
#print("*", stk[len(stk)-1], '\n')
print("Select", selection, '\n')
select()
select()
select()
back()
down()
select()
home()