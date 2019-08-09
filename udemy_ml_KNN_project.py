import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('C:\\Users\\siddhalo\\AppData\\Local\\Programs\\Python\\Python37\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\14-K-Nearest-Neighbors\\KNN_Project_Data.csv')
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
##
##sns.pairplot(df, hue='TARGET CLASS')
##plt.show()


scaler = StandardScaler()

scaler.fit(df.drop('TARGET CLASS', axis=1))

scaled = scaler.transform(df.drop('TARGET CLASS', axis=1))

df_scaled  = pd.DataFrame(scaled, columns=df.columns[:-1])
print(df_scaled.head())

X = df_scaled
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
##
##knn = KNeighborsClassifier(n_neighbors=1)
##
##knn.fit(X_train, y_train)
##
##
##pred = knn.predict(X_test)
##
##print(classification_report(y_test, pred))
##print(confusion_matrix(y_test, pred))
##
##

##error_rate = []
##
##
##for i in range(1, 40):
##    knn = KNeighborsClassifier(n_neighbors=i)
##    knn.fit(X_train, y_train)
##    pred_i = knn.predict(X_test)
##    error_rate.append(np.mean(pred_i != y_test))
##
##
##
##sns.lineplot(x=range(1,40), y=error_rate, markers=['O'])
##plt.show()
##


knn = KNeighborsClassifier(n_neighbors=37)

knn.fit(X_train, y_train)

pred = knn.predict(X_test)

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
