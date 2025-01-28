import joblib

model=joblib.load('genre-model.joblib')

result=model.predict([[1,35,1],[2,45,2]])
print(result)