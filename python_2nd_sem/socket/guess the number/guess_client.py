import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 1234))

while True:
    
    guess = input('Enter your guess: ')

    
    s.send(guess.encode())

   
    response = s.recv(1024).decode()

   
    print('Server:', response)

   
    if "Congrats" in response:
        break

s.close()
