import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df=pandas.read_csv("moviechoice.csv")

features=df[['gender','age','locality']]
labels=df['genre']

# 80% data for training the model and 20% data for testing
feat_train,feat_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2)

model=DecisionTreeClassifier()
model.fit(feat_train.values,labels_train.values)

result=model.predict(feat_test.values)
print('Predicted results -')
print(result)
print('Actual results -')
print(labels_test.values)
