"""
 Implements a simple socket server
"""

from re import A
import socket
import threading

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

empty_connections = []

def handle_client(client_connection):
    # Obtém o nome do utilizador
    username = client_connection.recv(1024).decode()
    user_connected = "You Are Now Connected, " + str(username) + "!"
    user_connected_public = str(username) + " Is Now Connected!"
    
    # Print username from client
    print(user_connected)

    # Send response to all clients
    for conn in empty_connections:
        if conn == client_connection:
            conn.send(user_connected.encode())
        else:
            conn.send(user_connected_public.encode())

    while True:
        msg = client_connection.recv(1024).decode()
        feedback = "(" + username + ") " + str(msg)
        
        # Terminate connection
        if msg == 'exit':
            feedback = "Goodbye " + str(username) + "!"
            # Send response to client
            client_connection.send(feedback.encode())
            break

        # Print message from client
        print(str(msg))

        # Send response to all clients
        for conn in empty_connections:
            conn.send(feedback.encode())

    # Close client connection
    print('Client disconnected...')
    client_connection.close()

    empty_connections.remove(client_connection)


while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Add connection to list
    empty_connections.append(client_connection)

    # Cria a Thread
    thread = threading.Thread(target=handle_client, args=[client_connection])

    thread.start()
    
# Close socket
server_socket.close()
