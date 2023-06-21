"""
 Implements a simple socket client
"""

import socket
import threading

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

def listening_thread(client_socket):
    while True:
        # Server Response
        res = client_socket.recv(1024).decode()
        print(res)
        
        # Check for exit
        if "Goodbye" in str(res):
            break

# Username
username = input('Username: ')
client_socket.send(username.encode())

# Login response
res = client_socket.recv(1024).decode()
print(res)

# Cria a Thread
thread = threading.Thread(target=listening_thread, args=[client_socket])
thread.start()

while True:
    # Send message
    msg = input('> ')
    client_socket.send(msg.encode())
    
    # Check for exit
    if "Goodbye" in str(res):
        break

thread.join()

# Close socket
client_socket.close()
