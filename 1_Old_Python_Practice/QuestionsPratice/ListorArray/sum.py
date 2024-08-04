lis1 = [1,2,3,4,5,6,93,5,3,7,5,0]

print(sum(lis1))
print(sorted(lis1))
lis1.reverse()
print(lis1)
print(min(lis1))
print(max(lis1))
print(len(lis1))

for index, el in enumerate(lis1,1):
    print(index," - ",el)