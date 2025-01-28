import pandas
from sklearn.tree import DecisionTreeClassifier

df=pandas.read_csv("moviechoice.csv")

features=df[['gender','age','locality']]
labels=df['genre']

model=DecisionTreeClassifier()
model.fit(features.values,labels.values)

result=model.predict([[2,25,1],[1,55,2]])
print(result)
