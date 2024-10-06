import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

server_socket.bind(server_address)
#0-65535

server_socket.listen(5)
client_socket, client_address = server_socket.accept()

client_socket.connect(server_address)

## Also you need to create a host and receiver