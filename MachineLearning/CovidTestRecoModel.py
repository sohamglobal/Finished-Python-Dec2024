from sklearn import tree
import pandas

df=pandas.read_csv("symptoms.csv")
print(df.head())
symptoms=df.iloc[:,:7]
result=df.iloc[:,7]

model=tree.DecisionTreeClassifier()
model.fit(symptoms.values,result.values)

reco=model.predict([[2,75,1,0,1,82,0]])
print(reco)

if reco[0]==1:
    print('Go and get yourself tested...dont panic')
else:
    print('Nothing looks serious..take the prescribed medicines')
    


