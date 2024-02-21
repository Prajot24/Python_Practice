from threading import*

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Class Hello")

class Hii(Thread):
    def run(self):
        for i in range(10):
            print("Class Hii")

P1 = Hello()
P2 = Hii()



P1.start()
P2.start()