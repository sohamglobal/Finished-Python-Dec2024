import json

mobile={
    "brand":"samsung",
    "model":"galaxy f23 5g",
    "color":"forest green",
    "ram":6,
    "rom":128,
    "screen":6.6,
    "battery":5000,
    "processor":"Q Snapdragon 750g",
    "price":13499.00
}


print(mobile)
print(type(mobile))

file=open("myphone.json","w")
json.dump(mobile,file)
file.close()
print('data written to JSON successfully')
