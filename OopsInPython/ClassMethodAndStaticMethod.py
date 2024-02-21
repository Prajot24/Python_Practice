class Person:
    Gender = "Male"
    def __init__(self,gender,age):
        self.Gender = gender
        self.age = age

    # @staticmethod
    # def changeGen(gender):
    #     Gender = gender
    
    @classmethod
    def changeGen(cls, gender,age):
        Gender = gender
        age = 22
        return cls(Gender,age)
    

P2 = Person.changeGen("Female",20)

P1 = Person("xyzzz",20)

# P1.changeGen("Female")
print(P1.Gender)
print(P2.Gender)