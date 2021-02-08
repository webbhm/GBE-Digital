'''
Example of a light helper function.
Create new files of this pattern for different experiment requirements.
This particular helper is a simple static lights on and off.
Import this file into a Light_Experiment.py file to adapt one or both behaviors

Author: Howard Webb
Date: 2/7/2021
'''
# PWM turn off setting
OFF = 100
# helper class to turn lights on and off
def on(light):
    # Set lights to static setting    
        light.set_lights(light.R, light.G, light.B, light.W)
        
def off(light):
    # Set lights to static setting    
        light.set_lights(OFF, OFF, OFF, OFF)
        
