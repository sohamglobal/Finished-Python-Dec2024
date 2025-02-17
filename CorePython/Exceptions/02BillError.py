
nm=input('Enter customer name : ')
try:
    amt=float(input('Enter purchase amount : '))
except:
    print('invalid amount')
    amt=0
finally:
    print('errors affect quality of code')

disc=amt*9/100
print('discount',disc)