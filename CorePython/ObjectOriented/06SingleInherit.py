#Single Inheritance - One base & One derived
#base class, super class, parent class
class One:
    def calcsum(self,a,b):
        s=a+b
        print('sum is',s)
    

#derived class, sub class, child class
class Two(One):
    def calcmulti(self,x,y):
        m=x*y
        print('multiplication is',m)


obj=Two()
obj.calcmulti(13,9)
obj.calcsum(45,79)



#AttributeError: 'Two' object has no attribute 'calcsum'