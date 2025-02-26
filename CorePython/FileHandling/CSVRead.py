file=open("students.csv","r")

for rec in file:
    #print(rec)
    #print(rec.split(','))
    print(rec.split(',')[0])



file.close()