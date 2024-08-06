arr = [2, 6, 8, 3, 2, 1]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j and arr[i]<arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        
print(arr)
my_list = []
for i in range(2,6):
    my_list.append(i)

print(my_list)