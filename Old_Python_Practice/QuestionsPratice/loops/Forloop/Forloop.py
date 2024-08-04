lis1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

ip = int(input("Enter Input: "))
for val in lis1:
    if(val==ip):
        print("Element is Present")
        break
else:
    print("Element not found")