import threading
import time

def print_message():
    while True:
        print("Hello, World!")
        time.sleep(2)


thread = threading.Thread(target=print_message)


thread.start()
