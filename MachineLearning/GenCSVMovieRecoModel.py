import pandas
from sklearn import tree

df=pandas.read_csv("genredataset.csv")
#print(df)
pandas.set_option('future.no_silent_downcasting', True)
#remove column Name as it is not needed for ML model
df=df.drop(columns=['Name'])
#print(df)

df['Gender']=df['Gender'].replace({'Male':1,'Female':2})
#print(df)
df['Locality']=df['Locality'].replace({'Rural':1,'Urban':2})
#print(df)
df['Education']=df['Education'].replace({'UG':1,'Grad':2,'PG':3})
#print(df)

#Build a ML model
features=df[['Age','Gender','Locality','Education']]
#print(features)
labels=df['Genre']
#print(labels)

model=tree.DecisionTreeClassifier()
model.fit(features.values,labels.values)

result=model.predict([[25,1,2,2],[55,2,1,1]])
print(result)