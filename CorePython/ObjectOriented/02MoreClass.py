class Calculator:
    def calcsquare(self,n):
        sq=n*n
        print('square of %d is %d' %(n,sq))
    
    def calcsum(self,a,b):
        c=a+b
        print('sum of %.2f and %.2f is %.2f' %(a,b,c))



c=Calculator()
c.calcsquare(13)
c.calcsquare(9)
c.calcsquare(26)
c.calcsquare(-45)

c.calcsum(35.89,72.14)
