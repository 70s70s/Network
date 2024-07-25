# Import the necessary module
from socket import *

# Define the port number on which the server will listen for incoming connections
serverPort = 12000

# Create a socket object for the server using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server socket to the specified port
serverSocket.bind(('', serverPort))

# Listen for incoming connections, with a maximum queue size of 1
serverSocket.listen(1)

# Print a message indicating that the server is ready to receive connections
print('The server is ready to receive')

# Enter an infinite loop to continuously accept and process connections
while True:
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()

    # Receive a sentence from the client, with a buffer size of 1024 bytes
    sentence = connectionSocket.recv(1024).decode()

    # Convert the received sentence to uppercase
    capitalizedSentence = sentence.upper()

    # Send the capitalized sentence back to the client
    connectionSocket.send(capitalizedSentence.encode())

    # Close the connection socket
    connectionSocket.close()
