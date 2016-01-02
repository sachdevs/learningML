from __future__ import division
import numpy as np
from numpy.linalg import lstsq
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training data for multiple regression
x = np.array([[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]])
y = np.array([[7], [9], [13], [17.5], [18]])

# test data
x_test = np.array([[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]])
y_test = np.array([[11],   [8.5],  [15],    [18],    [11]])

# Create and fit model
model = LinearRegression()
model.fit(x, y)
# print coefficient
print 'pearsons r'
print model.coef_
# print residual sum of squares
print 'residual sum of sq'
print np.mean((model.predict(x) - y) ** 2)

predictions = model.predict(x_test)
# real vs predicted print
for i, prediction in enumerate(predictions):
	print 'Predicted ' + str(prediction) + ' actual ' + str(y_test[i])

# r sq test
print 'rsq test'
print model.score(x_test, y_test)

plt.figure()
plt.title('Pizza vs Diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in $')

# make red regression line
plt.plot(x, model.predict(x), color='red')
# make black plot
plt.plot(x, y, 'k.')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()