arr = [1,2,3,4,5,6,7]
print(arr[::-1])

m = len(arr)/2

f = 0
l= len(arr)-1

for i in arr:
    while f<l:
        temp = arr[f]
        arr[f] = arr[l]
        arr[l] = temp
        f+=1
        l-=1
print(arr)