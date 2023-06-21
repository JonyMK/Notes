"""
 Implements a simple socket client
"""

import socket

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    # Ask a message to user
    msg = input("Mensagem: ")

    # Send message
    client_socket.send(msg.encode())

    if msg == "exit":
        break
    else:
        # Print message from server
        msg = client_socket.recv(1024).decode()
        print('Feedback From Server: ', msg)

# Close socket
client_socket.close()
