arr = [1,3,3,4,4,6,7,2,2,2,2,2,2,2]
count = {}

for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)
