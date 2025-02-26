file=open("aboutme.txt","r")

#print(file.readline())
#print(file.readline())

contents=file.read()
print(contents)

#lst=file.readlines()
#print(lst)

file.close()