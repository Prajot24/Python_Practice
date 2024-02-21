import threading
import time

def func(second):
    time.sleep(second)
    print(f"Sleep for {second}")




func(4)
func(3)
func(2)

t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[3])
t3 = threading.Thread(target=func,args=[2])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
