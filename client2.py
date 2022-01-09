
'''we have already implemented our Server Side which accepts 
or handles multiple clients connected simultaneously.Multiple
 clients can connect to the server and each time a client connects
  a corresponding thread is created for handling client requests
So, now we want to write the source code for the client-side 
so that the client can connect to the server we created.
So in this Client-Server, we need the same socket library 
to establish a connection with the Server-Side.'''

import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

''' to set up a connection using connect() 
of the socket library which establishes a 
connection with the server using the host 
and port we provided.'''


print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

'''we want is to make sure that the Client 
keeps running as the Server is Running. So 
for that, we need to use a while loop that.

And we also going to provide an input option
 to the client so that it can send data back
  to the Server and along with this we also use 
  the recv() function to receive data from Server Side'''

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()

#Socket Client Multithreading