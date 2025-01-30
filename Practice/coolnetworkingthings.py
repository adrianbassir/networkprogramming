import socket


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('google.com', 80)
connection.connect(addr)

print("Connection established")

num_bytes = connection.send(b'Hi!, Google! How are you?')
print(f"Sent: {num_bytes} bytes to {addr[0]}")

response = connection.recv(4096)

ascii_string = "Hi, Google! How are you?"
utf8_string = "Hi, GoÄgle! How are you?"

print(ascii_string)
print(utf8_string)

ascii_bytes = ascii_string.encode('ascii')
utf8_bytes = utf8_string.encode('utf-8')

print(ascii_bytes)
print(utf8_bytes)

connection.close()