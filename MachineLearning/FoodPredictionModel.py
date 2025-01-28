#Data preparation and ML Model
import pandas
from sklearn import tree
import joblib

df=pandas.read_csv('food.csv')
#print(df.head())
day_map={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
df['Day']=df['Day'].map(day_map)
print(df.head())

df['Gender']=df['Gender'].str.lstrip()
gender_map={'Male':1,'Female':2}
df['Gender']=df['Gender'].map(gender_map)

print(df.head())

features=df[['Day','Age','Gender']]
labels=df['Food']

model=tree.DecisionTreeClassifier()
model.fit(features.values,labels.values)

joblib.dump(model,'food-model.joblib')
print('food recommendation model saved for future use...')

