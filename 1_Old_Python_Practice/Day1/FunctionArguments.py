
def average(*number):
    sum =0
    for i in  number:
        sum=sum+i
    
    return sum/len(number)


d = average(1,2,3,4)
print(d)