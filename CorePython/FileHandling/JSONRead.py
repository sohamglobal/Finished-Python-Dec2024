import json

file=open("myphone.json","r")

data=json.load(file)
print(data)
print(data['color'])
print(data['price'])

file.close()