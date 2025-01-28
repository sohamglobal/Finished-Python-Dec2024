import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df=pandas.read_csv("moviechoice.csv")

features=df[['gender','age','locality']]
labels=df['genre']
total=0

for i in range(1,11):
    feat_train,feat_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2)

    model=DecisionTreeClassifier()
    model.fit(feat_train.values,labels_train.values)

    result=model.predict(feat_test.values)
    score=accuracy_score(result,labels_test)
    total+=score

#print(total)
print("Average Accuracy Score : %.2f%%" %((total/10)*100))
