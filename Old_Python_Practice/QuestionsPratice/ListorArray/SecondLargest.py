lis1 = [12,4,6,3,19,45,23]

l1 = lis1[0]
l2 = l1

for i in range(len(lis1)):
    if(l1<lis1[i]):
        l2 = l1
        l1 = lis1[i]
    elif(l2<lis1[i]):
        l2 = lis1[i]


print("Second Largest Value is ",l2)