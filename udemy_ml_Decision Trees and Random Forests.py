import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

"""
Index(['Kyphosis', 'Age', 'Number', 'Start'], dtype='object')
"""
df = pd.read_csv('C:\\Users\\siddhalo\\AppData\\Local\\Programs\\Python\\Python37\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\15-Decision-Trees-and-Random-Forests\\kyphosis.csv')

##print(df.head())
##print(df.columns)
##print(df.info())
##print(df.describe())
##

##sns.heatmap(df.isnull())
##plt.show()
##
##sns.pairplot(df, hue='Kyphosis')
##plt.show()


#df['Age_Years'] = df['Age'].apply(lambda x : int(x/12))

print(df.head())
##
##X = df.drop('Kyphosis', axis=1)
##y = df['Kyphosis']
##
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
##
##dcf = DecisionTreeClassifier()
##
##dcf.fit(X_train, y_train)
##
##pred = dcf.predict(X_test)
##
##print(classification_report(y_test, pred))
##print(confusion_matrix(y_test, pred))


X = df.drop('Kyphosis', axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

rfc = RandomForestClassifier(n_estimators=300)

rfc.fit(X_train, y_train)

pred = rfc.predict(X_test)

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

##error_rate=[]
##
##for i in range(200, 500):
##    rfc = RandomForestClassifier(n_estimators=i)
##    rfc.fit(X_train, y_train)
##    pred_i = rfc.predict(X_test)
##    error_rate.append(np.mean(pred_i != y_test))
##
##
##
##sns.lineplot(x=range(200, 500), y=error_rate)
##plt.show()

