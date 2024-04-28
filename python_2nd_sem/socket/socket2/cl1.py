
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('localhost',9094))

data = input('Client :' ).encode()
s.send(data)
res = s.recv(1024)
print('server', res.decode())
s.close()



