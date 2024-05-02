from threading import Thread

class B(Thread):
    def run(self):
        for i in range(5):
            print("Sanskar")

class A(Thread):
    def run(self):
        for i in range(5):
            print("Class A")

t1 = A()
t2 = B()

t1.start()
t2.start()
