import socket
import ipaddress

class Client:

    # constructor for Client class
    def __init__(self, ip: str, port: int, message: str):                
        self.ip = ip
        self.port = port
        self.message = message
    
    # function to send message from client to server
    def clientToServer(self):                                                 
        while True:
            # create a socket
            s = socket.socket() 
            # connect socket using ip address and port number                                              
            s.connect((self.ip, self.port))     
            # send message to the Server                              
            s.sendall(bytes(self.message, 'utf-8'))                           

            # recieve a message from the Server
            m = s.recv(64).decode('utf-8')                                    
            print('Message received from Server:' + m)

            s.close()
            # break the infinite loop if the user does not want to send anymore messages
            if input("Would you like to close the program?(Y/N): ") == "Y":   
                break
            # enter a new message to send to the Server
            self.message = input("please enter a message: ")                  


if __name__ == "__main__":
    # infinite loop, until a valid IP address is entered
    while True:                                                               
        try:
            ip = input("please enter an IP address: ")
            # checks if IP address is valid
            checkIP = ipaddress.ip_address(ip)                                
            break
        except ValueError:
            print("Error: NOT an IP address, please enter a valid IP address")
    # infinite loop, until a valid port number is entered
    while True:
        try:
            port = int(input("please enter a port number: "))
            if 1 > port or port > 65535:
                raise ValueError
            break
        except ValueError:
            print("Error: NOT a VALID port number, please enter a valid port number")
    message = input("please enter a message: ")
    client = Client(ip, port, message)
    client.clientToServer()