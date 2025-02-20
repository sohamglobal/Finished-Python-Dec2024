class Person:
    nm=None
    ct=None

    def takedata(self):
        nm=input('Enter your name : ')
        self.nm=nm
        self.ct=input('Enter city : ')
    
    def showdata(self):
        print('Name :',self.nm)
        print('City :',self.ct)


p=Person()
p.takedata()
p.showdata()

