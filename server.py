import socket
from socket import socket as SERVER


#server class
#the overall server object for a simple send-receive  client-server connection system
class Server:

    #server constructor
    #creates socket server object at the given IP and port
    def __init__(self, ipAddress : str, port: int):
        #server variables for later use
        self.addr : str = ipAddress
        self.port : int = port

        #run all necessary socket server functions
        #creates server object
        self.server : SERVER = SERVER(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.addr, self.port))

        #setup client system structure
        self.client = None
        self.clientAddr = None


    #main server function
    #loops until told to stop
    def run(self):
        #main loop
        while input("Close the server? (Y/N)") != "Y":
            print("Server Awaiting Connection...")

            #await connection
            self.server.listen()

            #accept connection
            self.client, self.clientAddr = self.server.accept()
            with self.client:
                print(f"Connected by {self.clientAddr}")

                #receive message from client
                while True:
                    data = self.client.recv(64).decode('utf-8')
                    if not data:
                        break

                    #send message to client
                    self.sendMessage(self.changeMessage(data))


    #send message method
    #send a connected client a message back
    def sendMessage(self, message : str):
        self.client.sendall(bytes(message, 'utf-8'))

    #change message method
    #given an input message (string), output the message in all capitals
    def changeMessage(self, message : str):
        return message.upper()




#main input validation loop
#if given valid info, will start server
def start():
    try:
        #asks for needed info
        suggestedPort = int(input("Please enter a port to use:"))
        myIP = socket.gethostbyname(socket.gethostname())
        print("Starting server on", myIP)

        #starts server
        server = Server(myIP, suggestedPort)
        server.run()

    #general error just restarts loop
    except Exception as e:
        print("Could not use suggested port. Please ensure port is a valid port number and is available")
        start()


#main function
if __name__ == "__main__":
    start()


    