class Student:
    nm='soham'

    def __init__(self):
        nm='ethan'
        print('local',nm)
        print('welcome',self.nm)
        self.nm='praffull'
    
    def thanks(self):
        print('thanks',self.nm)


s=Student()
s.thanks()