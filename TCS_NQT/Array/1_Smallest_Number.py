arr = [3,6,8,3,6,9,3,3,3]

b = 93829382839
c = 0

for i in arr:
    if i < b:  
        b=i  

print(b)

#with in built method
a = min(arr)
accurance = arr.count(a)
print(f'acuurance of {a} is {accurance}')

####### count accurance of max element

def count_max_accurance(arr):
    count = {}
    big = 219892
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in arr:
        if big > i:
            big = i
    
    return [count[big], big]

print(count_max_accurance(arr))
