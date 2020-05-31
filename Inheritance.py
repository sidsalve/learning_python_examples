class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
x=Person("Param","Gavhad")
x.printname()
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def welcome(self):
        print("welcome",self.fname,self.lname,"to the class of",self.graduationyear)
x1=Student("Param","Gavhad",2020)
x1.welcome()
x2=Student("Param","Gavhad",2020)
x2.printname()