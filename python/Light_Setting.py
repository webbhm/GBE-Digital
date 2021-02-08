'''
Template of Light Settings
Make a version of this file for each different experiment.
Import a Helper to control the behavior
Name the files "Light_Experiment_1.py", or appropriate number
Menu_Util.py will copy the selected experiment to "Light_Setting.py" where it will be
  available for the GrowLight class

Author: Howard Webb
Date: 2/7/2021
'''
from Light_Static_Helper import on
from Light_Static_Helper import off
args = {"setting":{"R": 70, "G":80, "B":60, "W":40}, "on_func":off, "off_func":on}

