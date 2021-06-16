'''
Main menu structure for GBE-D
This is a dictionary used to configure the menu and its behavior

"functions" are actions or display screens
Structure is as follows:
  name = what displayed in the title
  type = "function"
  module = python file to be imported
  class = class in the module to instantiate
  config = configuration for to dynamically create the display columns
  
"menu"
Tree of the displayed menu
structure is as follows:
  name = what is displayed on the menu item
  type = "menu"
  menu = set of items, either other menues or functions
  selection = currently highlighted menu item

Author: Howard Webb
Date: 2/16/2021
'''



# build Dashboard 
ds_func =  {"name":"Dashboard", "function":{"module":"Display_Dashboard", "class":"Dashboard", "config":"_column_list"}}
# build timelapse 
lapse_func = {"name":"Time Lapse", "function":{"module":"Display_Time_Lapse", "class":"TimeLapse", "config":"_column_list"}}
# build logo 
logo_func = {"name":"Logo", "function":{"module":"Display_Logo", "class":"DisplayLogo", "config":"_column_list"}}
# roll up to display menu
d_menu = []
d_menu.append(ds_func)
d_menu.append(lapse_func)
d_menu.append(logo_func)

# build display menu (time & temp)
disp_menu = {}
disp_menu["name"] = "Display Menu"
disp_menu["menu"] = d_menu

# build Select Experiment
e1_low_func = {"name":"Exp 1 High", "function":{"module":"Display_Exp", "class":"DisplayExp", "config":"_col_list"}}
e1_med_func = {"name":"Exp 1 Med", "function":{"module":"Display_Exp", "class":"DisplayExp", "config":"_col_list"}}
e1_high_func = {"name":"Exp 1 Low", "function":{"module":"Display_Exp", "class":"DisplayExp", "config":"_col_list"}}
# build Exp_2 menu
e2 = {"name":"Exp 2", "function":{"module":"Display_Exp", "class":"DisplayExp", "config":"_col_list"}}
# Exp 3
e3 = {"name":"Exp 3", "function":{"module":"Display_Exp", "class":"DisplayExp", "config":"_col_list"}}
# Ex[ 4
e4 = {"name":"Exp 4", "function":{"module":"Display_Exp", "class":"DisplayExp", "config":"_col_list"}}

sel_exp_menu = []
sel_exp_menu.append(e1_low_func)
sel_exp_menu.append(e1_med_func)
sel_exp_menu.append(e1_high_func)
sel_exp_menu.append(e2)
sel_exp_menu.append(e3)
sel_exp_menu.append(e4)
sel_menu = {}
sel_menu["name"] = "Select Exp"
sel_menu["menu"] = sel_exp_menu

# Build Custom Experiment
# Custom settings
rgbw_func = {"name":"Set RGBW", "function":{"module":"Display_CustomRGBW", "class":"CustomRGBW", "config":"_column_list"}}
set_on = {"name":"Set On", "function":{"module":"Display_CronTime", "class":"TimeOn", "config":"_column_list"}}
set_off = {"name":"Set Off", "function":{"module":"Display_CronTime", "class":"TimeOff", "config":"_column_list"}}
c_menu = []
c_menu.append(rgbw_func)
c_menu.append(set_on)
c_menu.append(set_off)
cust_menu = {}
cust_menu["name"] = "Custom"
cust_menu["menu"] = c_menu
# Build Experiment
plot_func = {"name":"Plot Random", "function":{"module":"Display_RandomConfirm", "class":"RandomConfirm", "config":"_column_list"}} # quick access to what testing
launch_func = {"name":"Launch", "function":{"module":"Display_Launch", "class":"Launch", "config":"_column_list"}}

exp_menu = []
exp_menu.append(sel_menu)
exp_menu.append(cust_menu)
exp_menu.append(plot_func)
exp_menu.append(launch_func)
exper_menu = {}
exper_menu["name"] = "Experiments"
exper_menu["menu"] = exp_menu

# Default Start up screen
dash_default = {"name":"Def Dashboard", "function":{"module":"Display_Default", "class":"DisplayDefault", "config":"_col_list"}}
lapse_default = {"name":"Def Lapse", "function":{"module":"Display_Default", "class":"DisplayDefault", "config":"_col_list"}}
logo_default = {"name":"Def Logo", "function":{"module":"Display_Default", "class":"DisplayDefault", "config":"_col_list"}}
def_menu = []
def_menu.append(dash_default)
def_menu.append(lapse_default)
def_menu.append(logo_default)
default_menu = {}
default_menu["name"] = "Default Display"
default_menu["menu"] = def_menu

#Setting menu
date_func = {"name":"Set Date", "function":{"module":"Display_SetDate", "class":"SetDate", "config":"_column_list"}}
time_func = {"name":"Set Time", "function":{"module":"Display_SetTime", "class":"SetTime", "config":"_column_list"}}
# Light Switch
switch_on = {"name":"Light On", "function":{"module":"Display_LightSwitch", "class":"LightSwitchOn", "config":"_column_list"}}
switch_off = {"name":"Light Off", "function":{"module":"Display_LightSwitch", "class":"LightSwitchOff", "config":"_column_list"}}

s_menu = []
s_menu.append(date_func)
s_menu.append(time_func)
s_menu.append(switch_on)
s_menu.append(switch_off)
s_menu.append(default_menu)
setting_menu = {}
setting_menu["name"] = "Settings"
setting_menu["menu"] = s_menu

# Demo
sunrise_func = {"name":"Sunrise", "function":{"module":"Display_SunriseDemo", "class":"SunriseDemo", "config":"_column_list"}}
kelvin_func = {"name":"Kelvin", "function":{"module":"Display_KelvinDemo", "class":"KelvinDemo", "config":"_column_list"}}
rainbow_func = {"name":"Rainbow", "function":{"module":"Display_RainbowDemo", "class":"RainbowDemo", "config": "_column_list"}}
dm_menu = []
dm_menu.append(sunrise_func)
dm_menu.append(rainbow_func)
dm_menu.append(kelvin_func)
demo_menu = {}
demo_menu["name"] = "Demo"
demo_menu["menu"] = dm_menu

upload_func = {"name":"Export Data", "function":{"module":"Display_Data", "class":"DisplayData", "config":"_column_list"}}
download_func = {"name":"Import Data", "function":{"module":"Display_UnderConstruction", "class":"DisplayText", "config":"_column_list"}}
clear_func = {"name":"Delete Data", "function":{"module":"Display_Data", "class":"DisplayData", "config":"_column_list"}}
dat_menu = []
dat_menu.append(upload_func)
dat_menu.append(download_func)
dat_menu.append(clear_func)
data_menu = {}
data_menu["name"] = "Data"
data_menu["menu"] = dat_menu

d_func = {"name":"Diagnostics", "function":{"module":"Display_UnderConstruction", "class":"DisplayText", "config":"_column_list"}}

# build home menu (display and exp)
h_menu = []
h_menu.append(disp_menu)
h_menu.append(exper_menu)
h_menu.append(setting_menu)
h_menu.append(data_menu)
h_menu.append(demo_menu)
h_menu.append(d_func)
main_menu = {}
main_menu["name"] = "Home Menu"
main_menu["menu"] = h_menu
main_menu["selection"] = 0

#print(main_menu, '\n')

def build_func(main_menu):
    # Convert the main menu into a dictionary of function
    # walk menu items
    func_list = {}
    #print(li)
    if "menu" in main_menu:
        #print(main_menu["name"])
        print(main_menu["menu"])
        for m in main_menu["menu"]:
            # recurse to get more functions
            func_list = {**func_list, **build_func(m)}
    elif "function" in main_menu:
        ref = main_menu["function"]
        func_list[main_menu["name"]] = ref
                
    #print(func_list)
    return func_list

# need to add menu as a function
func_list = {"menu":{"import":"menu", "class":"Menu"}}
func_list = {**func_list, **build_func(main_menu)}

def test():
    print("Test Menu")
    print(main_menu)
    # need to add menu as a function
    func_list = func_list = {"menu":"Menu"}
    func_list = {**func_list, **build_func(main_menu)}
    print(func_list)

if __name__ == "__main__":
    test()
    