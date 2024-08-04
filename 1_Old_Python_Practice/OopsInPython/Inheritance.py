class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def info (self):
        print(f"Id of {self.name} is {self.id}")

class Programmer(Employee):
    def role(self):
        print(f"He is a Programmer")

# emp = Employee("Prajot",20)
# emp.info()
    
p1 = Programmer("Rajesj",12)
p1.role()
p1.info()