import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training data
x = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]

# Create and fit model
model = LinearRegression()
model.fit(x, y)
# print coefficient
print model.coef_
# print residual sum of squares
print np.mean((model.predict(x) - y) ** 2)

plt.figure()
plt.title('Pizza vs Diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in $')

# make blue regression line
plt.plot(x, model.predict(x), color='red')
# make black plot
plt.plot(x, y, 'k.')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()