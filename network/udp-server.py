# Import the necessary module
from socket import *

# Define the port number on which the server will listen for incoming datagrams
serverPort = 12000

# Create a socket object for the server using UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the server socket to the specified port
serverSocket.bind(('', serverPort))

# Print a message indicating that the server is ready to receive datagrams
print("The server is ready to receive")

# Enter an infinite loop to continuously receive and process datagrams
while True:
    # Receive a datagram along with the client's address
    message, clientAddress = serverSocket.recvfrom(2048)

    print("Received message from client: ", message)
    # Decode the received message and convert it to uppercase
    modifiedMessage = message.decode().upper()

    # Send the modified message back to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
