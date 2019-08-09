import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn import metrics

df = pd.read_csv('C:\\Users\\siddhalo\\AppData\\Local\\Programs\\Python\\Python37\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\11-Linear-Regression\\USA_Housing.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
##
##sns.pairplot(df)
##plt.tight_layout()
##plt.show()


##sns.distplot(df['Price'])
##plt.show()


##sns.heatmap(df.corr(), annot=True)
##plt.tight_layout()
##plt.show()


X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y = df['Price']


"""
train and test split
"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

print(X_train.columns)
print(X_train.info())
print(X_test.info())

lm = LinearRegression()
lm.fit(X_train, y_train)

print(lm.intercept_)

print(lm.coef_)

cdf = pd.DataFrame(lm.coef_, X_train.columns, columns=['coeff'])
print(cdf)

predictions = lm.predict(X_test)

##
##plt.scatter(predictions, y_test)
##plt.show()
##
##sns.distplot((y_test-predictions))
##plt.show()

print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))

boston = load_boston()
print(type(boston))
dfb = pd.DataFrame(boston.data, columns=boston.feature_names)
print("\n\n")
print(dfb.head())
print(dfb.columns)
print(dfb.info())
X = dfb[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B']]
y = dfb['LSTAT']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
print(dfb.describe())


lm.fit(X_train, y_train)

dfc = pd.DataFrame(lm.coef_, X_train.columns, columns=['coef'])
print(dfc)

predictions = lm.predict(X_test)

sns.distplot((y_test-predictions))
plt.show()
