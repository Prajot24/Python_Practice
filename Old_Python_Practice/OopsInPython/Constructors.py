class Person:
    
    

    def __init__(self,name = None ,occ = None ):
        if(name==None or occ == None):
            print("Default Constructor")
        self.name = name
        self.occ = occ

   

    def info(self):
        print(f"{self.name} is {self.occ}")

P1 = Person("Prajot","Developer")
P2 = Person("Mani","HR")
P3 = Person()


P1.info()
P2.info()
P3.info()