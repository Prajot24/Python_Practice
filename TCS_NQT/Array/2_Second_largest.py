arr = [3,2,6,8,3,6,9,3,3,3,7,10]

first = -1
second = -1

for i in arr:
    if i > first:
        second = first
        first = i
print(second)
print()

##Second larget second Smallest number
def small_large_second(arr):
    first = -1
    second = -1

    small_one = float('inf')
    small_two = float('inf')

    for i in arr:
        if i > first:
            second = first
            first = i
        elif first> i >second:
            second = i

    for i in arr:
        if i < small_one:
            small_two = small_one
            small_one = i
        elif small_one < i < small_two:
            small_two =i

    return [second, small_two]


print(small_large_second(arr))