f=lambda n:n*n
print(f(9))

f=lambda amt:amt*10/100
print('Discount',f(15700))

f=lambda amt,disc:amt*disc/100
print('Discount :',f(23900,8))

f=lambda x,y:x*x+13*y+9
print(f(3,5))

'''
for i in range(1,11):
    print(f(i,i))
'''