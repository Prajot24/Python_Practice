#Map

def cube(a):
    return a*a*a

lis1 = [1,2,3,4,5,6,7,8,9]

newlis = list(map(cube,lis1))
print(newlis)

# Filter

def filterfun(a):
    if(a%2==0):
        return a

flis = list(filter(filterfun,lis1))
print(flis)

#Reduce
#First import reduce
from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)