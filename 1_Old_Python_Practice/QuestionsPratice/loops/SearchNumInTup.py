tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

a = 0
ip = int(input("Enter Number: "))

print(tup[0])

while a<len(tup):
    if(tup[a]==ip):
        print("Element at",a,"Index")
        break
    else:
        
        a=a+1