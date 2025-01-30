import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

our_address = ('0.0.0.0', 8888)
listen_socket.bind(our_address)

listen_socket.listen()

connection, address = listen_socket.accept()

print(f'Received connection from: {address}')

data = connection.recv(4096)

msg = data.decode('ascii')

print(f'Received message: {msg}')