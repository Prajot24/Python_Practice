class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Programmer(Employee):
    def __init__(self,name,age,role):
        super().__init__(name,age)
        self.role = role
    
    def info(self):
        print(f"My name is {self.name} and i am {self.age}. Working as {self.role}")

P1 = Programmer("Prajot",24,"Python Dev")
P1.info()