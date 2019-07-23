import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = sns.load_dataset('tips')

print(df1.columns)
print(df1.head())

##df1['total_bill'].plot.hist()
##plt.show()

df1.plot.bar()
plt.show()
