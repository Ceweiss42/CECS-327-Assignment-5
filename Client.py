import socket

class Client:

    def __init__(self, ip: int, port: int, message: str):        # constructor for Client class
        self.ip = ip
        self.port = port
        self.message = message
    
    def clientToServer(self):                                    # function to send message from client to server
        s = socket.socket()                                      # create a socket
        s.connect((self.ip, self.port))                          # connect socket using ip address and port number
        s.sendall(self.message)                                  # send message to the Server

        m = s.recv(1024)                                         # recieve a message from the Server

        while m:                                                 # infinite loop to get all messages from the Server
            print('Message received from Server:' + m)
            m = s.recv(1024)
        s.close()


if __name__ == "__main__":
    client = Client(input("please enter an ip: "), int(input("please enter a port: "), input("please enter a message: ")))
    client.clientToServer()