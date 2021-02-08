'''
Server part of the light service
Handles TCP message passing

Author: Howard Webb
Date: 2/8/2021
'''

import socket
import json

host = '' # change for internet service
port = 5562

class Server(object):
    
    def __init__(self, cmd_handler):
        self.s = self.setupServer()
        # custom function for handling commands/messages
        self.cmd_handler = cmd_handler

    def setupServer(self):
        # create a socket/port.  This will be active while the program is running
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created.")
        try:
            s.bind((host, port))
            s.listen(5)
        except socket.error as msg:
            print(msg)
        print("Socket bind complete.")
        return s

    def setupConnection(self):
        # Connections are set up for each interaction
        conn, address = self.s.accept()
        print("Connected to: " + address[0] + ":" + str(address[1]))
        return conn

    def dataTransfer(self, conn):
        # Generic handler of message traffic
        # Creates and destroys connections while the service is active
        while True:
            data = conn.recv(1024)
            txt = data.decode('utf-8')
            # Convert text to json/dictionary
            data = json.loads(text)
            print("Transfer", data)
            # need flag for when get EXIT message
            # call to custom command handler
            exit_flag, reply = self.cmd_handler.handle(data)
            # If get EXIT message, shut down the connection
            if exit_flag:
                break
            conn.sendall(str.encode(reply))
            print("Reply has been send.")
        print("Closing Connection")    
        conn.close()
        
