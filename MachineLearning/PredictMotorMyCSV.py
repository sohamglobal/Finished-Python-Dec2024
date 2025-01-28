from sklearn import tree
import pandas


df=pandas.read_csv("motorvehicle.csv")
#print(df.head())

features=df[['CC','Seats']]
labels=df['Observation']

clf=tree.DecisionTreeClassifier()
clf.fit(features.values,labels.values)

print(clf.predict([[110,2],[8000,3],[0,1]]))

