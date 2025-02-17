dic={
    'name':'praffull',
    'city':'london',
    'company':'sohamglobal',
    'mobile':'9890925745',
    'email':'913.ethanhunt@gmail.com',
    'dob':'9 June',
    'language':'english',
    'club':'chelsea',
    'home':'stamford bridge'
}

key=input('enter key : ')

try:
    print(dic[key])
except KeyError:
    print('key-value not found')

