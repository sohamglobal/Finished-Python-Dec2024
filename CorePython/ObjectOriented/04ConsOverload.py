class Employee:
    def __init__(self):
        print('welcome to office')
        print('-'*30)
    
    def __init__(self,nm):
        print('welcome %s to office' %nm)
        print('-'*30)

    def calctax(self,income):
        if income>500000:
            tax=income*3/100
        else:
            tax=0
        print('Tax',tax)


e1=Employee('joe root')
e1.calctax(750000)

# constructor overloading not available
#e=Employee()
#e.calctax(580000)
