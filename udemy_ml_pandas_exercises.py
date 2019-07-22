import pandas as pd
import numpy as np

sal = pd.read_csv('C:\\Users\\Siddharth\\AppData\\Local\\Programs\\Python\\Python36\\sf-salaries\\Salaries.csv')
print(sal.head())
print(sal.shape)
print(sal.columns)
print(sal.info())


#print(sal['BasePay'].mean())
#print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])

print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName'])

#print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()])['EmployeeName']
print(sal.iloc[sal['TotalPayBenefits'].argmin()]['EmployeeName'])
print(sal.groupby('Year'))
print(sal.iloc[sal['TotalPayBenefits'].argmin()])
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()])
#print(sal.groupby('Year').mean()['BasePay'])
print(sal['JobTitle'].nunique())
print(sal['JobTitle'].value_counts().head(5))

print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1))

def chief_title(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(lambda x : chief_title(x))))

sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len', 'JobTitle']].head())
print(sal[['TotalPayBenefits', 'title_len']].corr())
