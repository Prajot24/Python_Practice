#Sets are unordered collection of data items. 
# They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are unchangeable, meaning you cannot change items of the set once created. 
# Sets do not contain duplicate items.
sett = {2,4,"prajot",6,"p","d",6}
print(sett)


# empty set
set1 = set()
print(type(set1))

#You can access items of set using a for loop.
for i in sett:
    print(i,end=",")

