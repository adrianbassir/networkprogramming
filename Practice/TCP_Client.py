import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('127.0.0.1', 8888)
connection.connect(addr)

print('Connected to server')

msg = 'Hello World!'
msg_encoded = msg.encode('ascii')
connection.send(msg_encoded)