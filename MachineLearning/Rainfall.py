from sklearn import tree

#cloud,wind,rain,thunderstorms
features=[[1,1,0,0],[0,1,0,0],[2,1,1,0],[2,2,3,0],[3,2,2,1]]
labels=['no umbrella','no umbrella','umbrella','raincoat','stay home']

clf=tree.DecisionTreeClassifier()
clf.fit(features,labels)

print(clf.predict([[2,3,2,0]]))
