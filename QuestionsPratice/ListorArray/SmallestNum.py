list1 = [10,3,6,2,8,7]

min = list1[0]

for i in range(len(list1)):
    if(list1[i]<min):
        min=list1[i]

print(min)