import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',9094))


server.listen(1)
print('waiting for connection')

client, address = server.accept() 
print('connected')

server.send('welcome to sankhuz localhost'.encode())


server.close()