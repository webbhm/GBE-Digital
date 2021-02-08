'''
Stand-in Server for testing
NOTE: may need to add logic for converting date from text to json/dictionary
'''
import json

class Server(object):
    
    def __init__(self, cmd_handler):
        self.cmd_handler = cmd_handler

    def dataTransfer(self, text):
        data = json.loads(text)
        reply = self.cmd_handler.handle(data)
        print("Reply has been send.", reply)
        print("Closing Connection")    
        return reply
