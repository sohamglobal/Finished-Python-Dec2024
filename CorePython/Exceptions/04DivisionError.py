try:
    a=int(input('Enter first number : '))
    b=int(input('Enter second number : '))
    c=a/b
except ValueError:
    a=1
    b=1
    print('invalid input')
    c=a/b
except ZeroDivisionError:
    b=1
    c=a/b
    print('divide by zero avoided')


print('result of division is %.2f' %c)


'''
Traceback (most recent call last):
  File "F:\August2022-Python\Exceptions\04DivisionError.py", line 4, in <module>
    c=a/b
ZeroDivisionError: division by zero
'''