try:
    a=int(input('Enter first number : '))
    b=int(input('Enter second number : '))
    c=a/b
#except ValueError,ZeroDivisionError:
except:
    print('cant calculate...')
    c=1


print('result of division is %.2f' %c)
