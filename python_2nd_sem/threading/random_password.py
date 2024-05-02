import threading
import random
import string

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(f"Generated Password: {password}")

def password():
    length = int(input("Enter the length of the password: "))
    
    thread = threading.Thread(target=generate_password, args=(length,))
    thread.start()
    thread.join() 
    
password()

