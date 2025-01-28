from sklearn import tree
import pandas


df=pandas.read_csv("auto.csv")
#print(df.head())

features=df[['engine_cc','seats','wheels']]
labels=df['vehicle_type']

clf=tree.DecisionTreeClassifier()
clf.fit(features.values,labels.values)

print(clf.predict([[110,2,2],[8000,3,4]]))

