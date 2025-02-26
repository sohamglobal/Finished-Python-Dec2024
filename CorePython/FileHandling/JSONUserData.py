import json

nm=input('enter name ')
city=input('enter city ')
mob=input('Enter mobile number ')
eml=input('enter email ID ')

dic={}
dic['name']=nm
dic['city']=city
dic['mobile']=mob
dic['email']=eml

print(dic)

file=open("user.json","w")
json.dump(dic,file)
print('done...')
file.close()

