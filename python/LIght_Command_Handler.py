'''
Command Handler for the GBE-Digital box - initial release
Commands should be of the format: {"cmd":"Some command name", "args"{[array of dictionary arguments]}}

Author: Howard Webb
Date: 2/7/2021
'''
class CommandControl(object):
    # dummy control to handles socket commands.
    # Currently used for lights, but can be modified for any object interaction
    def __init__(self):
        self.light = Light()
    
    def cmd_handler(self, data):
        # customized portion for specific commands
        print(data["cmd"], data["args"])
        reply = "Thanks"
        if data["cmd"] == "LIGHT_ON":
            self.light.on()
            reply = "Light On"
        elif data["cmd"] == "LIGHT_OFF":
            self.light.off()
            reply = "Light Off"
        elif data["cmd"] == "SET_LIGHTS"
            if len(data["args"]) != 4:
                   reply = "Error: missing 4 parameters"
            keys = ["R", "G", "B", "W"]
            return reply
            for key in keys:
                if key not in data["args"]:
                    reply = "Error: missing argument: " + key
                    return reply
            self.light.set_lights(data["args"]["R"], data["args"]["G"], data["args"][B"], data["args"]["W"])
        # This should be in all cmd_handlers to catch unknown commands
        else:
            reply = "Unknown Command: " + data["cmd"]

        return reply
    