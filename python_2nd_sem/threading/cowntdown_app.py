import threading

import time

def cowntdown1():
    print("countdown starts :")
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)
    print("time expired")
    
t1 = threading.Thread(target=cowntdown1)

t1.start()
        