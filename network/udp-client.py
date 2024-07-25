# Import the necessary module
from socket import *

# Define the server's hostname and port number
serverName = 'localhost'  
serverPort = 12000

# Create a socket object for the client using UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    # Prompt the user to input a lowercase sentence
    message = input('Input lowercase sentence: ')

    # Send the message to the server using UDP
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # Receive the modified message from the server, with a buffer size of 2048 bytes
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # Print the modified message received from the server
    print(modifiedMessage.decode())

# Close the client socket
clientSocket.close()
