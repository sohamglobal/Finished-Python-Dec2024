class Praffull:
    def __init__(self,nm):
        print(nm)


class Sharayu(Praffull):
    def __init__(self):
        print('class sharayu')
        super().__init__('spider')


obj=Sharayu()
#obj.show()



