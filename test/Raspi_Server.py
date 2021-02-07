import socket
host = ''
port = 5562

def getTemp():
    return 23.4, 32.5

def command_handler(data):        
    # generic handler for testing
    # cmd is in dictionary structure
    reply = 'Thanks'
    command = data['cmd']

    print("Received:", command)
    if command == 'LIGHT_ON':
        reply = self.light.on()
    if command == 'LIGHT_OF':
        reply = self.light.off()
    if command == 'LIGHT_SET':
        r = data["args"]['r']
        g = data["args"]['g']
        b = data["args"]['b']
        w = data["args"]['w']                
        reply = self.light.set(r, g, b, w)
    if command == 'GET_TEMP':
        temp, humidity = getTemp()
        reply = 'humidity: {:0.2f}% temperature: {:0.2f}C'.format(humidity, temp)
        
    elif command == 'DATA':
        dataMessage = data.split(":", 2)
        humidity = dataMessage[1]
        temperature = dataMessage[2]
        print("Received: " + humidity + " : " + temperature)
    elif command == 'EXIT':
        print("Disconnected with Client")
        break
    else:
        reply = 'Unknow Command:' + command
        print(reply)
    return reply



from GrowLight import GrowLight
        
class LightControl(object):
    # manage socket and light
    
    def __init__(self):
        self.light = GrowLight()
    def on():
        return 'Light Turned On'
    
    def off():
        return 'Light turned off'
    
    def set(r, g, b, w):
        return "Light set"
    
    def command_handler(data):        
        # handler for light commands
        # cmd is in dictionary structure
        reply = 'Thanks'
        command = data['cmd']

        print("Received:", command)
        if command == 'LIGHT_ON':
            reply = self.light.on()
        if command == 'LIGHT_OF':
            reply = self.light.off()
        if command == 'LIGHT_SET':
            r = data["args"]['r']
            g = data["args"]['g']
            b = data["args"]['b']
            w = data["args"]['w']                
            reply = self.light.set(r, g, b, w)
        elif command == 'EXIT':
            print("Disconnected with Client")
            break
        else:
            reply = 'Unknow Command:' + command
            print(reply)
        return reply
    

class LightServer(object):
    
    def __init__(self, cmd_handler=command_handler):
        self.s = self.setupServer()
        self.cmd_handler = cmd_handler

    def setupServer(self):
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
        conn, address = self.s.accept()
        print("Connected to: " + address[0] + ":" + str(address[1]))
        return conn

    def dataTransfer(conn):
        while True:
            data = conn.recv(1024)
            data = data.decode('utf-8')
            print(data)
            reply = cmd_handler(data)
            '''
            dataMessage = data.split(":", 2)
            command = dataMessage[0]
            print("Received:", command)
            if command == 'LIGHT_ON':
                reply = self.light.on()
            if command == 'LIGHT_OF':
                reply = self.light.off()
            if command == 'LIGHT_SET':
                reply = self.light.set(r, g, b, w)
            if command == 'GET_TEMP':
                temp, humidity = getTemp()
                reply = 'humidity: {:0.2f}% temperature: {:0.2f}C'.format(humidity, temp)
                
            elif command == 'DATA':
                dataMessage = data.split(":", 2)
                humidity = dataMessage[1]
                temperature = dataMessage[2]
                print("Received: " + humidity + " : " + temperature)
            
            elif command == 'EXIT':
                print("Disconnected with Client")
                break
            else:
                reply = 'Unknow Command:' + command
                print(reply)
            '''    
            conn.sendall(str.encode(reply))
            print("Reply has been send.")
        print("Closing Connection")    
        conn.close()
        

s = LightServer()
while True:
    try:
        conn = s.setupConnection()
        s.dataTransfer(conn)
    except Exception as e:
        print(e)
        break