class Car():
    def __init__(self,na,pri):
        self.name = na
        self.price = pri
    
    
    @property
    def get_name(self):
        return self.name
    
    @get_name.setter
    def get_name(self,newname):
        self.name = newname
        
    

C1 = Car("Honda",10000)
C1.get_name = "tata"
print(C1.get_name)


