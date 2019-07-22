import pandas as pd
import numpy as np
##########################Pandas Series #########################

#built on numpy arrays

data = [10, 20, 30]
labels = ['a', 'b', 'c']
arr = np.array([1,2,3])
d = {'a':10, 'b':20, 'c':30}

print(pd.Series(data))
print(pd.Series(data, labels))
print(pd.Series(arr, labels))
print(pd.Series(d))

ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], ['USA', 'Italy', 'India', 'USSR'])

print(ser1)
print(ser2)
print(ser1['USA'])
print(ser1+ser2)

##########################Pandas Dataframes #########################

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df['W'])
print(type(df['W']))
print(df[['W', 'X']])

print("\n\n\n\n")
print(df.drop(['W', 'X'], axis=1))
print(df)
print('\n\n\n\n')
print(df.drop('A'))
print(df.drop(['A', 'B'], axis=0))
print(df)

df['new'] = df['X']+df['Y']
print(df)

"""
selecting rows
"""
print('\n\n\n\n')
print(df.loc['A'])
print(df.loc[['A', 'B']])
print('\n\n')
print(df.iloc[0])
print(df.iloc[[0, 1]])
print('\n')
print(df.loc[['A', 'D'], ['X', 'Y']])
print(df.loc[['A', 'B', 'C'], ['X', 'Y', 'Z']])

## conditional selection
print('\nconditional selection')
print(df[df['W']>0])
print(df[(df['W']>0) & (df['Y']<0)])
print(df[(df['X']<0) | (df['Z']>1)])

## setting and resetting index
print('\n\n')
print(df.reset_index())
print('\n')

newind = 'CA CH DF KG KF'.split()
df['States'] = newind
print(df)
print(df.set_index('States', inplace=True))
print(df)

## multi level index ##
print('\n\n')
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2), hier_index, ['A', 'B'])
print(df)
#print(df.loc['G1'].loc['1'])

################## Missing Data ##################

## drop na

d = {'A':[1, np.nan, 3], 'B':[4,5,8], 'C':[np.nan, np.nan, 6]}
df = pd.DataFrame(d)
print('\n\n')
print(df)
print(df.dropna(axis=1))
print(df.fillna(value='FILL VALUE'))
print(df['A'].fillna(value=df['A'].mean()))
print(df)
df['A'] = df['A'].fillna(value=df['A'].mean())
print(df)
print(list(df.columns))

print('\n\n\n')

print(df)

for col in list(df.columns):
    df[col] = df[col].fillna(value = df[col].mean())

print(df)


################## group by ##################

d = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 'Person':['Sid', 'stacy', 'john', 'lombard', 'Chris', 'Lionel'],'Sales':[123,435,623,143,123,543]}
df = pd.DataFrame(d)
print('\n\n')
print(df)
print(df.groupby('Company').describe().transpose())


################# merging, joining and concatenating ###############
print('\n\n')
df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'], 'B':['B0', 'B1', 'B2', 'B3'],'C':['C0', 'C1', 'C2', 'C3'], 'D':['D0', 'D1', 'D2', 'D3']}, index=[0,1,2,3])
df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'], 'B':['B4', 'B5', 'B6', 'B7'], 'C':['C4', 'C5', 'C6','C7'], 'D':['D4', 'D5', 'D6', 'D7']}, index=[4,5,6,7])
print(df1)
print('\n\n')
print(df2)

print(pd.concat([df1, df2]))
print('\n\n')
print(pd.concat([df1, df2], axis=1))
#merge on a key
print('\n\n')
left = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],'B':['B0', 'B1', 'B2', 'B3'], 'key':['K0', 'K1', 'K1', 'K2']}, index=[0,1,2,3])
right = pd.DataFrame({'C':['C0', 'C1', 'C2', 'C3'], 'D':['D0', 'D1', 'D2', 'D3'], 'key':['K0', 'K0', 'K1' , 'K1']}, index=[0,1,2,3])
print(pd.merge(left, right, how='inner', on='key'))
print('\n')
print(pd.merge(left, right, how='outer', on='key'))



# join - same as merge except it is on index instead of a column

left = pd.DataFrame({'A':[45,65,76], 'B':[23,65,98]}, index=[0,1,2])
right = pd.DataFrame({'C':[45,73,89], 'D':[23,664,64]}, index=[0,2,3])
print('\n\n')
print(left.join(right))
print('\n\n')
print(left.join(right, how='outer'))

################# operations ####################
print('\n\n\n\n')
df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[111, 222, 444, 444], 'col3':['assa', 'asdas', 'asdas', 'rwwwg']})
print(df)
# print unique

print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

## conditional selection
print(df[df['col2']>2])
print(df[(df['col1']>1) & (df['col2']>100)])

## apply method - apply some processing to each element in a column
print('\n')
def times2(num):
    return num*2

print(df['col1'].apply(times2))

print(df['col3'].apply(len))

print(df['col1'].apply(lambda x : x+2))

#dropping columns
print(df.drop('col1', axis=1))

#attributes

print(df.columns)
print(df.index)

#sorting

print(df.sort_values(by='col2'))


#################### data input and output #####################


df = pd.read_csv('//csv//file//path//abcd.csv')
df.to_csv('//sdf//sdf//efgh.csv', index=False) // # index=False else index will also be stored as a column


