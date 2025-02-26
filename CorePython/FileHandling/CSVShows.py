file=open("NetflixOriginals.csv","r")
tot=-1
cnt=0

for rec in file:
    tot+=1
    try:
        if float(rec.split(',')[3])>7:
            cnt+=1
    except:
        pass


print('total shows released by netflix are',tot)
print('shows with IMDB rating more than 7 are',cnt)
perc=cnt*100/tot
print('hit shows %.2f%%' %perc)
file.close()
