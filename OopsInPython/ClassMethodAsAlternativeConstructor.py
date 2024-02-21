class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))


P1 = Person.from_string("Prajot,30")
print(P1.age)
print(P1.name) 