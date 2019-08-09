import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


tips = sns.load_dataset('tips')
print(tips.head())


################ Distribution Plots ###################
##sns.distplot(tips['total_bill'], kde=False, bins=40)
##plt.show()


##sns.jointplot(x='total_bill', y='tip', data=tips)
##plt.show()
##

##
##sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
##plt.show()
##
##sns.pairplot(tips)
##plt.show()


##sns.pairplot(tips, hue='sex')
##plt.show()


##sns.rugplot(tips['total_bill'])
##plt.show()

##sns.kdeplot(tips['total_bill'])
##plt.show()


##################### Categorical Plots ########################3
##
##sns.barplot(x='sex', y='total_bill', data=tips)
##plt.show()


sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
