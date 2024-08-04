emp = {1:"prajot",2:"sourabh",3:"rohit",4:"mani"}
emp1 = {5:"suresh",6:"ramesh",7:"rajesh"}
print(emp)
#throw error if element is not present
print(emp[4])
#print none if element is not present 
print(emp.get(3))

#for keys in dic
print(emp.keys())

#for values in dic
print(emp.values())

#add emp1 to emp
emp.update(emp1)
print(emp)

#emp.clear() to ceare dictionary

# emp.pop("pass key")

# emp.popitem() last element remove
