#server.py

import socket
from socket import socket as SERVER


'''
Requirements:

 - receive message from client
 - change the message to capital letters
 - send changed message back to client
 - should be able to send multiple messages
 - use an infinite loop to stay open

'''

class Server:

    def __init__(self, ipAddress : str, port: int):
        self.addr : str = ipAddress
        self.port : int = port
        self.server : SERVER = SERVER(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.addr, self.port))
        self.client = None
        self.clientAddr = None

    def run(self):
        print("Server Awaiting Connection...")
        self.server.listen()
        self.client, self.clientAddr = self.server.accept()
        with self.client:
            print(f"Connected by {self.clientAddr}")
            while True:
                data = self.client.recv(64)
                if not data:
                    break
                self.sendMessage(self.changeMessage(data))
        


    #send message method
    #send a connected client a message back
    def sendMessage(self, message : str):
        self.client.sendall(message)

    #change message method
    #given an input message (string), output the message in all capitals
    def changeMessage(self, message : str):
        return message.upper()




def start():
    try:
        suggestedPort = int(input("Please enter a port to use:"))
        myIP = socket.gethostbyname(socket.gethostname())
        server = Server(myIP, suggestedPort)
        server.run()

    except Exception as e:
        print("Could not use suggested port. Please ensure port is a valid port number and is available")
        start()

if __name__ == "__main__":
    start()


    