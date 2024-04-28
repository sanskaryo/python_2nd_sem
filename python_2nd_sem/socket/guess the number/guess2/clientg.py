import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('localhost',1023))

while 1:
    message=input('client').encode()
    s.send(message)
    data=s.recv(1024)
    print('server:',data)

s.close()