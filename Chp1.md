##Basic terms
Supervised - training set has right wrong to guide learning in the right direction
Unsupervised - do pattern finding/matching on training set 

Response var - output
Features - input vars
Explanatory vars - phenomena features measure
training set - used to train program
test set - used to test program

##Machine Learning Tasks
Classification tasks - predict values for DISCRETE response vars using explanatory vars. (i.e. stock price go up or down)
Regression tasks - predict values for continuous response vars
- both require supervised learning
Clustering tasks - group related observations
- clustering is used to explore dataset
- i.e. cluster by genres for internet radios
- unsupervised
Dimensionality Reduction Tasks - for datasets with millions of explanatory variables, use only vars that have greatest effect on response
- unsupervised
- i.e. data vis

##Training data and Test data
Over-fitting - memorizing training set
- bad because memorize noise and outliers
- balancing memorization and generalization = over fitting vs underfitting
Validation set - sometimes required to tune variables called hyperparameters (control how program is learned)
Cross validation - when training data is scarce: section data into parts, train on all but one, test on last one. Train with new set every time and test with a new remaining partition

##Performance measures, bias, and variance
-Two causes of prediction error: bias & variance
Bias - a model with high bias will produce similar output regardless of the training data
Variance - a model with high variance will produce very different output depending on its training data
-ideally low bias, low variance
Measures of accuracy - rate or true positives and true negatives/ all possible errors and positives (bayes theorem, sensitivity and specificity measures)

```
accuracy:
ACC = (TP + TN)/(TP + TN + FP + FN)
percision:
P = TP/(TP + FP)
recall:
R = TP/(TP + FN)
```
