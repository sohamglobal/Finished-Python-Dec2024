import pandas
from sklearn.tree import DecisionTreeClassifier
import joblib

df=pandas.read_csv("moviechoice.csv")

features=df[['gender','age','locality']]
labels=df['genre']

model=DecisionTreeClassifier()
model.fit(features.values,labels.values)

joblib.dump(model,'genre-model.joblib')
print('your model is saved for future use')