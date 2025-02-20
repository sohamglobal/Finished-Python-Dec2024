#Multiple inheritance
class One:
    def calcsum(self,a,b):
        s=a+b
        print('sum is',s)
    
class Two:
    def calcmulti(self,x,y):
        m=x*y
        print('multiplication is',m)

class Three(Two,One):
    def calcsquare(self,n):
        sq=n*n
        print('square is',sq)


obj=Three()
obj.calcsquare(65)
obj.calcmulti(75,23)
obj.calcsum(29,54)