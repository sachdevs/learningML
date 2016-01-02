from __future__ import division
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training data
x = np.array([6, 8, 10, 14, 18])
y = np.array([7, 9, 13, 17.5, 18])
a = x.reshape(5,1)
b = y.reshape(5,1)

# Create and fit model
model = LinearRegression()
model.fit(a, b)
# print coefficient
print model.coef_
# print residual sum of squares
print np.mean((model.predict(a) - y) ** 2)

# calculate xmean and ymean
xbar = np.mean(x)
ybar = np.mean(y)

# calculate var(x)
varx = np.var(x, ddof=1)

# calculate covar(x,y)
covxy = np.cov(x, y)[1][0]

#print calculations and calc alpha and beta vals
print 'cov(x,y) is ' + str(covxy)
print 'var(x) is ' + str(varx)
beta = covxy/varx
alpha = ybar - (xbar*beta)
print 'beta is ' + str(beta)
print 'alpha is ' + str(alpha)

plt.figure()
plt.title('Pizza vs Diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in $')

# make red regression line
plt.plot(a, model.predict(a), color='red')
# make black plot
plt.plot(x, y, 'k.')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()