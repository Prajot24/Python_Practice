from functools import cache
import time

@cache
def checkfun(n):
    time.sleep(5)
    return n*5

print(checkfun(10))
print(checkfun(20))
print(checkfun(30))
print("After Cache")
print(checkfun(10))
print(checkfun(20))
print(checkfun(30))
