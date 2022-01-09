# import the socket library to establish a connection
#  and thread library for multithreading.
import socket
import os
from _thread import *

#create a socket connection using the socket() of 
# the socket library
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0

#bind the host and port to the socket server we created 
# above in the program.

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

# create a function that handles requests from the 
# individual client by a thread.

'''defined a new function named threaded_client
In this function, we are using the recv() function
 to get data from each client independently and then 
 we simply return the reply to the particular client 
 with the same message with string concatenate 
 “Server Says” in the beginning'''
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


# we want is to run our Server all the time, which means 
# we don’t want to make that our Server get stopped.

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()

#Socket server side