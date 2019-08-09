import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("KNNData.csv", index_col=0)

print(df.head())
print(df.columns)
print(df.info())
print(df.describe())

##
##sns.heatmap(df.isnull())
##plt.show()

print(df['TARGET CLASS'].unique())


scaler = StandardScaler()

scaler.fit(df.drop('TARGET CLASS', axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

df_scaled = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print(df_scaled.head())


X_train, X_test, y_train, y_test = train_test_split(df_scaled, df['TARGET CLASS'], test_size=0.3, random_state=101)

knn = KNeighborsClassifier(n_neighbors=35)

knn.fit(X_train, y_train)

predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))


##
##error_rate = []
##
##for i in range(1, 40):
##    knn = KNeighborsClassifier(n_neighbors=i)
##    knn.fit(X_train, y_train)
##    pred_i = knn.predict(X_test)
##    error_rate.append(np.mean(pred_i != y_test))
##
##
##sns.lineplot(x=range(1, 40), y=error_rate, color='b', markers=['O'])
##plt.show()
