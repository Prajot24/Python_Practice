import time

timestamp = time.strftime("%H:%M:%H")
print(timestamp)
a= int(timestamp[0:2])
print(a)

if(a<12):
    print("Good Morning")
elif(a>12 and a<17):
    print("Good Afternoon")
else:
    print("Good night")