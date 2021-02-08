'''
Command Handler for the GBE-Digital box - initial release
Limited originally to:
Turn lights on
Turn lights off
Set lights to an rgbw value
Commands should be of the format: {"cmd":"Some command name", "args"{[array of dictionary arguments]}}

Author: Howard Webb
Date: 2/7/2021
'''

class CommandControl(object):
    # dummy control to handles socket commands.
    # Currently used for lights, but can be modified for any object interaction
    def __init__(self, light):
        # Instance of light object
        self.light = light
    
    def handle(self, data):
        # customized portion for specific commands
        # flag for controlling connection exiting
        exit_flag = False
        print("In cmd_handler")
        #print("Text", text)
        #print(data, type(data))
        # Generic reply
        reply = "Thanks for using the GBE-Digital"
        # Turn the lights on
        if data["cmd"] == "LIGHT_ON":
            self.light.on_func(self.light)
            reply = "Light On"
        # turn the lights off
        elif data["cmd"] == "LIGHT_OFF":
            self.light.off_func(self.light)
            reply = "Light Off"
        # set the lights to a specific value set
        elif data["cmd"] == "LIGHT_SET":
            reply = "Light Set"
            # validate that have 4 values
            if len(data["args"]) != 4:
                   reply = "Error: missing 4 parameters"
                   return reply
            # validate that have the correct parameters
            keys = ["R", "G", "B", "W"]
            for key in data["args"]:
                 #print(key)
                 if key not in keys:
                     reply = "Error: missing argument: " + key
                     return reply
            # pass the arguments to the light
            self.light.set_lights(data["args"]["R"], data["args"]["G"], data["args"]["B"], data["args"]["W"])
        # This should be in all cmd_handlers to catch unknown commands
        elif data["cmd"] == "EXIT":
            reply = "Exit"
            # make sure this is set to close the socket connection
            exit_flag = True
        # Catch-all for what don't understand
        else:
            reply = "Unknown Command: " + data["cmd"]

        return exit_flag, reply
    