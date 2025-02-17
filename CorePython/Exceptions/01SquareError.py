try:
    no=int(input('Enter a number '))
except:
    print('invalid value..please enter a number')
    no=0

sq=no*no
print('square is',sq)


'''
Exception handling is a process of preventing a program
from getting abnormally terminated due to runtime errors

step-1 : find out the line/lines in the program which
can result into an error

step-2 : enclose the lines inside try block

step-3 : write code to recover from the error in 
except block

'''