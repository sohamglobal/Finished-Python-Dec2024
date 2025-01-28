import numpy 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate data for the model
numpy.random.seed(0)
house_sizes=numpy.random.randint(800,3000,50)
#print(house_sizes)

prices=50 * house_sizes + 30000 + numpy.random.randint(-50000,50000,50)
#print(prices)

house_sizes=house_sizes.reshape(-1,1)
print(house_sizes)

# split data for training and testing
sizetrain,sizetest,pricetrain,pricetest=train_test_split(house_sizes,prices,test_size=0.2,random_state=42)

#create model
model=LinearRegression()
model.fit(sizetrain,pricetrain)

# make predictions
predictions=model.predict(sizetest)

# plot the data
plt.scatter(sizetest,pricetest,color='blue',label='Actual prices')
plt.plot(sizetest,predictions,color='red',label='Predicted prices')
plt.xlabel('House size')
plt.ylabel('Price')
plt.legend()
plt.title('House price prediction')
plt.show()