import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost',1023))

actual_no='17'

s.listen(1)

print('waiting for connection')

c1,address=s.accept()

while 1:
    #c1.send(b'welcome to gla local server)
    data=c1.recv(1024)
    if data.decode()>actual_no:
        d='number is larger'
    elif data.decode()<actual_no:
        d='number is less'
    else:
        d='you guessed it right'

    print('client',data.decode())

    #data=input('server').encode()
    c1.send(d.encode())

c1.close()