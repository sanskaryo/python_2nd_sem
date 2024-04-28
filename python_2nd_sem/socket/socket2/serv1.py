# 0 to 1024 RE UNDESIRABLE PORT NUMBER AS THEY ARE OCCUPIED BY OS


import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9094))
s.listen(2)
print("Waiting for connection...")

while 1:
    
    client,addr = s.accept()
    print('connection established',addr)
    data = client.recv(1024)
    print('Client:','Hello sanskar')
    client.send('Hello sanskar')
    print('Echo sent')
    client.close()

