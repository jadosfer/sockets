from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 20064))

s.send(b"Soy el cliente y me la banco!")
s.recv(8192)
