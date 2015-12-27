#2 - Linear Regression
##Simple linear regression
- Used to model relationship between one response variable and one explanatory variable
- Assumes linear relationship exists between response(Price) and explanatory vars(Diameter) called a *hyperplane*
- to test whether or not variables are independent use chi square tests of independence
- *hyperplane* - subspace that has one var less than the space that contains it
- *subspace* - (remember lin alg) Let V be a vector space over the field K, and let W be a subset of V. Then W is a subspace if and only if W satisfies the following three conditions:
  1. The zero vector, 0, is in W.
  2. If u and v are elements of W, then the sum u + v is an element of W;
  3. If u is an element of W and c is a scalar from K, then the product cu is an element of W
- for one explanatory var and one response var (=> 2 dimensions), hyperplane has to be 1-dimensional aka line.
- alpha - y-int
- beta - slope
- sklearn.linear_model.LinearRegression class is an estimator
- called method of least square cause minimizing sum of square of y-difference of points from line (residuals)

##Evaluating fitness of model with cost function
- *cost function* used to messure error in model
- *residuals* difference in prediction by model and irl
- *prediction errors* difference between predicted vals and observed vals
- *residual sum of squares* should be minimized:
  - aka mean of predict - y squared

```
SS _res = sum(1, n, i, (y _i - f(x _i))^2)
```

##Solving ordinary least squares for simple linear regression
- Calculating param values - alpha and beta
- Beta is a function of variance of x and covariance of x and y

```
var(x) = sum(1, n, i, (x_i - xbar)^2/(n-1))
np.var(x, ddof=1) -> ddof is bessel's correction
```

- *Bessel's correction* that n-1 in formula for sample variance and sample mean
- *covariance* is measure of how two variables change together, i.e. how linear they are.
- if cov = 0, no linear relationship exists b/w vars. However vars may still not be independent (chi sq test)

```
cov(x,y) = sum(1, n, i, (x _i - xbar)(y _i - ybar)/(n-1))
np.cov(x, y)[0][1] -> since covariance of x, y is located in matrix entry [0][1] or [1][0]
```

- then the formula for beta is:

```
Beta = cov(x,y)/var(x)
```

- now we can solve for alpha because we know the line must pass through xbar and ybar:

```
Alpha = ybar - beta*xbar
```

- 