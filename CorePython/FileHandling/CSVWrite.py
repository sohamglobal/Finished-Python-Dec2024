snm=input('enter student name ')
qual=input('enter qualification ')
age=int(input('enter age '))
course=input('enter course ')
city=input('enter city ')

file=open("students.csv","a")

file.write(snm+','+qual+','+str(age)+','+course+','+city+'\n')
print('data written to csv successfully')
file.close()