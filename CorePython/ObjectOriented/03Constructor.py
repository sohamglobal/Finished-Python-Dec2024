# constructor is a special function in a class that runs automatically when object is created

class Billing:
    def __init__(self):
        print('welcome to Python shop')
        print('-'*30)

    def calcnetbill(self,amt):
        disc=amt*9/100
        net=amt-disc
        print('Amount',amt)
        print('Discount',disc)
        print('Netbill',net)


obj=Billing()
obj.calcnetbill(23570.00)
