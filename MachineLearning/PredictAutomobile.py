#pip install scikit-learn
from sklearn import tree

features=[[800,5],[1200,5],[150,2],[7500,2],[4500,3],[125,2],[350,2],[1500,5]]
labels=['car','car','motor cycle','truck','truck','motor cycle','motor cycle','car']

clf=tree.DecisionTreeClassifier()
clf.fit(features,labels)

print(clf.predict([[110,2],[8000,3]]))

