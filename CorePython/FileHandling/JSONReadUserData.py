import json

file=open("user.json","r")
data=json.load(file)

#print(data)

for it in data.items():
    print(it)


file.close()