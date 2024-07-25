# Import the necessary module
from socket import *

# Define the server's hostname and port number
serverName = 'tcp-server'
serverPort = 12000

# Create a socket object for the client
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect the client socket to the server
clientSocket.connect((serverName, serverPort))

while True:
    # Prompt the user to input a lowercase sentence using Python's input function
    sentence = input('Input lowercase sentence: ')

    # Encode the sentence into bytes and send it to the server
    clientSocket.send(sentence.encode())

    # Receive the modified sentence from the server, with a buffer size of 1024 bytes
    modifiedSentence = clientSocket.recv(1024)

    # Print the modified sentence received from the server
    print('From Server:', modifiedSentence.decode())

    # Close the client socket
clientSocket.close()
