lst=[5,1,7,9,9,1,4,9,1,8]
unique=[]

[unique.append(item) for item in lst if item not in unique]
print(unique)

