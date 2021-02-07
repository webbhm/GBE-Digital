class Light(object):
    # dummy light object
    def light_on(self):
        return "On"
    def light_off(self):
        return "Off"
    

class Control(object):
    # dummy light control, handles socket commands and light
    def __init__(self):
        self.light = Light()
    
    def cmd_handler(self, data):
        print(data["cmd"], data["args"])
        reply = "Thanks"
        if data["cmd"] == "LIGHT_ON":
            self.light.light_on()
            reply = "Light On"
        return reply
    

class TestSocket(object):
    # dummy socket function
    def __init__(self, cmd_ctl):
        # pass command controler as function so socket can handle different command sets
        print("init TS")
        self.cmd_ctl = cmd_ctl
        #print(self.cmd_ctl)
        
    def run(self, data):
        print("Run")
        reply = self.cmd_ctl(data)
        print(reply)
        
def test():
    ts = TestSocket(Control().cmd_handler)
    # fake data command
    data = {"cmd":"LIGHT_ON", "args":{'r':12, 'g':45, 'b':55, 'g':99, 'w':77}}
    # fake socket call
    ts.run(data)
        
if __name__ == "__main__":
    test()