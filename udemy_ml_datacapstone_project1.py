import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

calls = pd.read_csv('C:\\Users\\Siddharth\\AppData\\Local\\Programs\\Python\\Python36\\montcoalert\\911.csv')
##print(calls.shape)
##print(calls.columns)
##print(calls.head())
##print(calls.describe)
##print(calls.info())
##
##print(calls['zip'].value_counts().head())
##
##print(calls['twp'].value_counts().head())
##
##print(calls['title'].unique())
##print(calls['title'].nunique())
##
calls['Reason'] = calls['title'].apply(lambda x : x.split(':')[0])
##print(calls['Reason'].head())
##print(calls['Reason'].unique())
##
##print(calls['Reason'].value_counts())

##sns.countplot(x='Reason', data=calls)
##plt.show()
##


##print(type(calls['timeStamp'].iloc[0]))

calls['timeStamp'] = pd.to_datetime(calls['timeStamp'])
##print(type(calls['timeStamp'].iloc[0]))
##
##print(calls['timeStamp'].head())
##print(calls['timeStamp'].iloc[0].hour)

calls['hour'] = calls['timeStamp'].apply(lambda time : time.hour)
calls['month'] = calls['timeStamp'].apply(lambda time : time.month)
calls['day of week'] = calls['timeStamp'].apply(lambda time : time.dayofweek)

##print(calls.head())

dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
calls['day of week'] = calls['day of week'].map(dmap)
##print(calls[['hour', 'month', 'day of week']].head())
##
##sns.countplot(x='day of week', data=calls, hue='Reason')
##plt.show()


byMonth = calls.groupby('month').count()
##print(byMonth)
##byMonth['lat'].plot.line()
##plt.show()

##
##sns.lmplot(x='month',y='twp', data=byMonth.reset_index())
##plt.show()

calls['Date'] = calls['timeStamp'].apply(lambda time : time.date())
##print(calls['Date'].head())

byDate = calls[calls['Reason']=='EMS'].groupby('Date').count()
##byDate['lat'].plot.line()
##plt.tight_layout()
##plt.show()
##
##calls_pivot = pd.pivot_table(calls, index='day of week', columns='hour', values='Reason', aggfunc=np.sum)
##print(calls_pivot)


##byDayHour = calls.groupby(['day of week', 'hour']).count()['Reason'].unstack()
##sns.heatmap(byDayHour)
##plt.show()


byDayMonth = calls.groupby(['day of week', 'month']).count()['Reason'].unstack()
sns.clustermap(byDayMonth)
plt.show()
