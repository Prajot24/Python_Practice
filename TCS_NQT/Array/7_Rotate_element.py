arr = [1,2,3,4,5]

# inp = input('Enter Number: ')

for i in range(2):
    first = arr[0]
    for j in range(len(arr)-1):
        arr[j] = arr[j+1]      
    arr[len(arr)-1] = first   


print(arr)