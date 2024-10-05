import socket

#Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Define the host and port to connect to
host = '127.0.0.1'
port = 12345


#Connect to the server
server_socket.connect((host, port))

#Start listening to incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}....")

#Accept the connection and get the client socket
client_socket, client_address = server_socket.accept()
print(f'Connection established with {client_address}')

#Receive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f"Received: {data}")

#Echo the data received back to the client
client_socket.send(data.encode('utf-8'))

#Close the sockets
client_socket.close()
server_socket.close()