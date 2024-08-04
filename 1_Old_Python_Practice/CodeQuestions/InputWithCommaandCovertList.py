
num = input("Enter number with comma to add list: ")

lis1 = num.split(",")
print(lis1)
lis2=[]
for i in lis1:
    lis2.append(int(i))

print(lis2)