# CECS 327 Assignment 5
 REPO for CECS 327 group project
 
 #Instructions for Users
 
 ##Client.py
 
 Please use the Client.py file to run the client side of the program. It is recommended to run the Server.py file BEFORE the client, so you know what IP to input. Client.py file will first ask for an IP address to connect to input the IP into the console.
 Then, it will ask for a port. Ensure that the port number you use is the same port number as specified on the server.
 Finally, it will ask for a message. This message prompt will be sent to the server, and awaits a response. Once sent, you have the option of quitting by typing 'n' or sending another message (by simply not sending 'n' but another message).
 
 ##Server.py
 
 Please use Server.py for the server side of the program. The Server.py script, when run will ask for a port number. Once input, it will respond with a confirmation that the server is running. This response contains the port and IP of the server. This information needs to be passed on to the client.py script. Once the port is input, no new things need to be done to the Server. It will continually run until told to stop via Ctrl+C.
