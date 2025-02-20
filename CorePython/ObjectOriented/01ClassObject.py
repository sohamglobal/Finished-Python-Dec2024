class User:
    def welcome(self):
        print('welcome to OOP in Python')
        print('-'*45)
    
    def thanks(self,nm):
        print('thanks %s for joining sohamglobal' %nm)


obj=User()
obj.welcome()
obj.thanks('praffull')



# TypeError: User.welcome() takes 0 positional arguments but 1 was given