import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen(2)
print("Waiting for connection...")

    
client,addr = s.accept()
print('connection established',addr)

while 1:
    data = client.recv(1024)
    if not data:
        break
    print('Client:',data.decode())
    data = input('Server: ').encode()
    client.send(data)
    print('Echo sent')
client.close()