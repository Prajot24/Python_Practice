class Person:
    name = "prajot"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

    @classmethod
    def from_int(cls, userNum,age ):
        # cls(userNum,age)
        
        return cls.name
	    
            
		
# P2 = Person.from_int(23,3)
# print(P2.name)

# print(Person.name) class level change

P1 = Person("ABCD",22)
print(P1.from_int("ds",23))

# print(P1.name)
print(P1.from_int("ww",2))

