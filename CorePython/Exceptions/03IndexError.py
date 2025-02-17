lst=['microsoft','oracle','google','accenture','volkswagen','bmw','vmware','dell']

try:
    n=int(input('Enter index : '))
except ValueError:
    n=0
    print('invalid input..reset to zero')



try:
    print(lst[n])
except IndexError:
    print('element number does not exist in the list')




