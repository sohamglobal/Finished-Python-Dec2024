class Product:
    quantity=0
    purchcost=0

    def __init__(self,quantity,purchcost):
        self.quantity=quantity
        self.purchcost=purchcost
    
    def showstock(self):
        print('Quantity      : %d' %self.quantity)
        print('Purchase Cost : %d' %self.purchcost)

    def __add__(self,sam):
        q=self.quantity+sam.quantity
        c=self.purchcost+sam.purchcost
        return Product(q,c)


print('-------APPLE------------')
apple=Product(6,415750)
apple.showstock()

print()
print('--------SAMSUNG---------')
samsung=Product(15,327600)
samsung.showstock()

print('--------TOTAL-----------')
total=apple+samsung
total.showstock()

#TypeError: unsupported operand type(s) for +: 'Product' and 'Product'

