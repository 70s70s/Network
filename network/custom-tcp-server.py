from socket import *
import os
import time
from datetime import datetime
serverPort = 3126
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Print a message indicating that the server is ready to receive connections
print("The server is ready to receive")
def last_modified_time(filename):
    return time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(os.path.getmtime(filename)))
# Enter an infinite loop to continuously accept and process connections
while True:
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()  
  # Print a message indicating that a connection has been established
    print("Connection established with", addr) 
    # Receive a line of input from the client
    sentence = connectionSocket.recv(1024).decode()
    # If the client closes the connection or sends an empty message, break the loop
    if not sentence:
        break 
    # Print the received line onto the server's standard output
    print(sentence)
    # Prepare the HTTP response to send back to the client
    httpResponse = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nLast-Modified: {}\r\n\r\n<html><body><h1>Hello World</h1></body></html>\r\n".format(last_modified_time("custom-tcp-server.py")) 
    # Send the HTTP response back to the client
    connectionSocket.send(httpResponse.encode())
    # Close the connection socket
    connectionSocket.close()

    