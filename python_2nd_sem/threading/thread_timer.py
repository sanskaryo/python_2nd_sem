import threading
import time

def time_expire():
   print("Timer Expired")

def delay():
   T = int(input("Enter the delay time (in seconds): "))
   timer = threading.Timer(T, time_expire)
   timer.start()

delay()
