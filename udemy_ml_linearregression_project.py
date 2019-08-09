import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
"""
['Email', 'Address', 'Avatar', 'Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership', 'Yearly Amount Spent']
"""


df = pd.read_csv('C:\\Users\\siddhalo\\AppData\\Local\\Programs\\Python\\Python37\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\11-Linear-Regression\\Ecommerce Customers')


print(df.head())
print(df.info())
print(df.columns)
print(df.describe()[['Time on App', 'Time on Website']])



##sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df)
##plt.show()


##sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)
##plt.show()


##sns.jointplot(x='Time on App', y='Length of Membership', data=df, kind='hex')
##plt.show()


##sns.pairplot(df)
##plt.show()


##sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=df)
##plt.show()


X = df[[ 'Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression()

lm.fit(X_train, y_train)

dfc = pd.DataFrame(lm.coef_, X_train.columns, columns=['coeff'])
print(dfc)

predictions = lm.predict(X_test)
##
##sns.distplot((y_test-predictions))
##plt.show()              


##
##plt.scatter(y_test, predictions)
##plt.show()
print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))


