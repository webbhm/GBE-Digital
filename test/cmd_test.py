'''
test function to play with configuring a generic Socket_Server to handle different commands.
This concept passes parameters through the TCP command
Will not use parameters for lights, as the settings are in experiment files.
Will keep this parameter architecture as it may be used for future functionality for other objects
Commands should be of the format: {"cmd":"Some command name", "args"{[array of dictionary arguments]}}

Author: Howard Webb
Date: 2/7/2021
'''

class Light():
    # dummy light object
    def on(self):
        return "On"
    def off(self):
        return "Off"
    

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
        # This should be in all cmd_handlers to catch unknown commands
        else:
            reply = "Unknown Command: " + data["cmd"]

        return reply
    

class TestSocket(object):
    # dummy socket object
    def __init__(self, cmd_ctl):
        # pass command controler as function so socket can handle different command sets
        print("init TS")
        self.cmd_ctl = cmd_ctl
        #print(self.cmd_ctl)
        
    def run(self, data):
        # fake transmission receiver
        print("Received command")
        reply = self.cmd_ctl(data)
        print(reply)
        
def test():
    # Exercise a simulated message sending
    ts = TestSocket(CommandControl().cmd_handler)
    # fake data command
    data = {"cmd":"LIGHT_ON", "args":[{'r':12}, {'g':45}, {'b':55}, {'g':99}, {'w':77}]}
    # fake sending of TCP message to a socket
    ts.run(data)
        
if __name__ == "__main__":
    test()