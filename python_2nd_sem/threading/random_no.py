import threading
import random
import time

def generate_number():
    for _ in range(5):
        number = random.randint(1, 100)
        print(number)
        time.sleep(1)

def number():
    thread = threading.Thread(target=generate_number)
    thread.start()
    thread.join()

number()