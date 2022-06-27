import socket
import sys  # python module for accessing the parameters in the script
import json  # Module used for exchanging structured data between processes

class Communication:

# Module to manage the process communication based on TCP sockets
# Player1 will be playing on the server side and player2 will be the remote client
# create the client and server sockets after initialization of the game
# Start server part first otherwise the client will fail to connect

    def __init__(self, comm_role):  # comm_role will be server or client

        # Initialize server host:port
        self.host = socket.gethostname() # as server and client run both on the same machine for this demo
        self.port = 5009  # initiate port no above 1024
        # Create socket instance
        self.local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance

        # if socket instance to be configured as server
        if (comm_role == 'server'):

            self.local_socket.bind((self.host, self.port))  # bind host address and port together

            # configure how many client the server can listen simultaneously
            self.local_socket.listen(1)
            print("Server start listen")
            # accept client ... client_con is the client connection and will be used during the program execution
            self.client_con, self.address_client = self.local_socket.accept()  # accept new connection. It will wait until a connection is requested
            print("Connection from: " + str(self.address_client))
        # if socket instance is a client
        elif (comm_role == "client"):
            # socket used to connect to the server
            self.local_socket.connect((self.host, self.port))
            print("Connection established to the server")

    def get_message_from_client(self):
        data = ""
        while not data:  # wait until response is sent
            data = json.loads(self.client_con.recv(1024).decode("UTF-8"))  # receive response
            if not data:
                # if data is not received break and start new iteration of the while oop
                break
            return data

    def send_message_to_client(self, request_type, message):
        # request_type could be Shot, Hit, ...
        # message: could be Shot coordinate, Hit result, ...
        data = {"type": request_type, "content": message}
        self.client_con.send(json.dumps(data).encode("UTF-8"))  # send data to the client

    def get_message_from_server(self):
        data = json.loads(self.local_socket.recv(1024).decode("UTF-8"))  # receive response
        return data

    def send_message_to_server(self, request_type, message):
        # request_type could be Shot, Hit, ...
        # message: could be Shot coordinate, Hit result, ...
        data = {"type": request_type, "content": message}
        self.local_socket.send(json.dumps(data).encode("UTF-8"))  # send data to the client

    def close(self):
        self.local_socket.close()  # close the connection