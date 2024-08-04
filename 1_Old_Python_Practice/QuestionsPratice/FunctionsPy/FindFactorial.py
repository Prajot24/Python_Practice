a = int(input("Enter number: "))

def factorial(b):
    fact = 1
    for i in range(1,b+1):
        fact = fact*i
        i+=1
    return fact

print(factorial(a))