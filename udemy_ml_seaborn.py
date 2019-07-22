import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

################### distribution plots #######################

x = np.linspace(0,5,11)
y = x**2
tips = sns.load_dataset('tips')
##print(tips.shape)
##print(tips.columns)
print(tips.head())
##
##sns.distplot(tips['total_bill'])
##plt.show()

##
##sns.jointplot(x='total_bill', y='tip', data=tips)
##plt.show()

##
##sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
##plt.show()

##sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
##plt.show()
##
##sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
##plt.show()


##
##sns.pairplot(tips, hue='time')
##plt.show()





########################### categorical plots ######################3
##
##sns.barplot(x='sex', y='tip', data=tips)
##plt.show()

##sns.barplot(x='sex', y='tip', data=tips, estimator=np.std)
##plt.show()

##
##sns.countplot(x='sex', data=tips)
##plt.show()

##sns.barplot(x='day', y='total_bill', data=tips ,hue='sex')
##plt.show()
##
##sns.boxplot(x='day', y='total_bill', data=tips, hue='sex')
##plt.show()

##
##sns.countplot(x='day', data=tips)
##plt.show()

##sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')
##plt.show()

##
##sns.stripplot(x='day', y='total_bill', data=tips)
##plt.show()

##sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)
##plt.show()


"""
general plotting method
"""
##
##sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')
##plt.show()


################### matrix plots ######################

flights = sns.load_dataset('flights')
print(flights.head())

tc = tips.corr()
print(tc)
fp = flights.pivot_table(index='month', columns='year', values='passengers')
print(fp.head())

##sns.heatmap(tc, annot=True)
##plt.show()

##
##sns.heatmap(fp)
##plt.show()


##sns.clustermap(fp)
##plt.show()


#################### Grids ###########################

iris = sns.load_dataset('iris')
print(iris.head())
print(iris['species'].unique())
##sns.pairplot(iris)
##plt.show()

##
##g = sns.PairGrid(iris)
##g.map(plt.scatter)
##plt.show()

##g = sns.PairGrid(iris)
##g.map_diag(sns.kdeplot)
##g.map_upper(plt.scatter)
##g.map_lower(sns.swarmplot)
##plt.show()

##g = sns.FacetGrid(data=tips, row='time', col='smoker')
##g.map(sns.distplot, 'total_bill')
##plt.show()


################### Regression Plots ###################
##
##sns.lmplot(x='total_bill', y='tip', data=tips)
##plt.show()

##sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'])
##plt.show()
##
##sns.lmplot(x='sepal_length', y='petal_length', data=iris, hue='species', markers=['o','v','x'])
##plt.show()
##
##sns.lmplot(x='total_bill', y='tip', data=tips, row='sex', col='time', aspect=0.6, size=8)
##plt.show()


"""
    styling
"""

sns.set_style('whitegrid')
sns.lmplot(x='total_bill', y='tip',data=tips, col='sex', palette='seismic')
plt.show()
