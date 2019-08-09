import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


"""
['Daily Time Spent on Site', 'Age', 'Area Income',
       'Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country',
       'Timestamp', 'Clicked on Ad']
"""

df = pd.read_csv('C:\\Users\\siddhalo\\Documents\AWS\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\13-Logistic-Regression\\advertising.csv')

print(df.head())
print(df.info())
print(df.columns)
print(df.describe())
##
##sns.heatmap(df.isnull())
##plt.show()

##
##sns.distplot(df['Age'])
##plt.show()


##
##sns.jointplot(x='Age', y='Area Income', data=df)
##plt.show()

##
##sns.jointplot(x='Age', y='Daily Time Spent on Site', data=df, kind='kde')
##plt.show()
##
##sns.pairplot(df, diag_kind='hist', hue='Clicked on Ad')
##plt.tight_layout()
##plt.show()

X = df[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage','Male']]
y = df['Clicked on Ad']
y = df['Clicked on Ad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

logreg = LogisticRegression()

logreg.fit(X_train, y_train)

predictions = logreg.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
