#guess the number 

import socket 
import random


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 1234))

s.listen(1)
print('Guess the number game')
print('waiting for connections')

actual_no= random.randint(1,20)
print(actual_no)

s.listen(1)

client,address=s.accept()

while 1:
    
    data = client.recv(1024).decode()
    if not data:
        break
    guess = int(data)
    if guess > actual_no:
        client.send("Sorry, the number is smaller than your guess.".encode())
    elif guess < actual_no:
        client.send("Sorry, the number is larger than your guess.".encode())
    else:
        client.send("Congrats! You got it correct.".encode())
        break
client.close() 
s.close()
        
        
