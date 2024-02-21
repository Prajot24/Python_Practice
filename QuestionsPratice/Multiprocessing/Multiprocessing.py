import multiprocessing
import time

def func(number):
    for i in range(number):
        time.sleep(0.6)
        print("Square ",i*i)

def func1(number):
    time.sleep(0.6)
    for i in range(number):
        print("Cube is ",i*i*i)

if __name__ == '__main__':

    m1 = multiprocessing.Process(target=func,args=[5])
    m2 = multiprocessing.Process(target=func1,args=[5])

    m1.start()
    m2.start()

    m1.join()
    m2.join()

    print("Python Course Completed")