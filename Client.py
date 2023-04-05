import socket
from time import sleep

class Client:

    def __init__(self, ip: str, port: int, message: str):                     # constructor for Client class
        self.ip = ip
        self.port = port
        self.message = message
    
    def clientToServer(self):                                                 # function to send message from client to server
        while True:
            s = socket.socket()                                               # create a socket
            s.connect((self.ip, self.port))                                   # connect socket using ip address and port number
            s.sendall(bytes(self.message, 'utf-8'))                           # send message to the Server

            m = s.recv(64).decode('utf-8')                                    # recieve a message from the Server
            print('Message received from Server:' + m)

            s.close()
            if input("Would you like to close the program?(Y/N): ") == "Y":   # break the infinite loop if the user does not want to send anymore messages
                break
            self.message = input("please enter a message: ")                  # enter a new message to send to the Server


if __name__ == "__main__":
    client = Client(input("please enter an ip: "), int(input("please enter a port: ")), input("please enter a message: "))
    client.clientToServer()