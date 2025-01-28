import joblib

model=joblib.load('food-model.joblib')

result=model.predict([[5,34,1],[1,29,2]])
print(result)