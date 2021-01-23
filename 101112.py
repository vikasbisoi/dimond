# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:56:10 2021

@author: admin
"""

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("D:/diamonds-m.csv")
 
#########################################################################################################
#Q10

print("====================================================================")
print("Mean of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].mean())

print("====================================================================")        
print("Count of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].count())

print("====================================================================")        
print("Sum of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].sum())

print("====================================================================")        
print("The quartile summary of each column are:")
df.quantile([0.25,0.50,0.75])

#########################################################################################################
#Q11

print("====================================================================")
print("variance of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].var())
print("====================================================================")
print("Standard deviation of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].std())

print("====================================================================")        
for column in df.columns:
    if(df[column].dtype!=object):
        print("Maximum value of column",column,":",df[column].max())
        print("Minimum value of column",column,":",df[column].min())
        print("Range of column",column,":",df[column].max()-df[column].min())
        print("#############################################################")

print("====================================================================")
##########################################################################################################
#Q12
print("================================================================================")
print("count of outliers and their value for each numeric column")
print("================================================================================")
for column in df.columns:
    if(df[column].dtype!=object):
        if(column!='id'):
            q1, q3= np.percentile(df[column],[25,75])
            iqr = q3 - q1
            lower_bound = q1 -(1.5 * iqr) 
            upper_bound = q3 +(1.5 * iqr) 
            print("Interquartile range of column",column,":",iqr)
            print("Lower bound of column ",column,":",lower_bound)
            print("Upper bound of column ",column,";",upper_bound)
            outlier=[]
            for i in (df[column]):
              if lower_bound>i:
                   outlier.append(i)
              if upper_bound<i:
                   outlier.append(i)
            print("Outliers are:",outlier)
            print("Number of outliers in column",column,"are:",len(outlier))
            if not outlier:
              print("No Outlier Present")
             
            print("=================================================================================")
            print("=================================================================================")
############################################################################################################
#Q14
plt.figure(figsize=(10,10))
df.hist(sharey=True,align="mid")
plt.tight_layout()
plt.show()
############################################################################################################

###########################################################################################################
#Q8
print("=================================================================================")
for column in df.columns:
    if df[column].dtype!=object:
        if column!='id':
            print("number of null vallues in column",column,":",df[column].isnull().sum())
            df[column]=df[column].fillna(df[column].median())
            print("number of null vallues in column",column," after replacing it with median:",df[column].isnull().sum())
            print("----------------------------------------------------------------------------")
print("=================================================================================")
###############################################################################################################
#Q18
print("=================================================================================")
m=(np.mean(df.x)+np.mean(df.y))/2

df["ideal_depth"]=df.z/m


df["Difference"]=df["depth"]-df["ideal_depth"]
print(df["Difference"])
print("=================================================================================")
################################################################################################################
print("=================================================================================")
print("\n-----Obvious Errors-----")
pd.options.display.float_format = '{:,.2f}'.format
for colName in df.columns:
    if  df[colName].dtype == 'object':
        print("Unique values in",colName,"\n",df[colName].unique())        
print("=================================================================================")