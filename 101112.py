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
print("Mean of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].mean())
        
print("Count of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].count())
        
print("Sum of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].sum())
        
print("The quartile summary of each column are:")
df.quantile([0.25,0.50,0.75])
#########################################################################################################
#Q11
print("variance of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].var())
        

print("Standard deviation of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].std())
        
for column in df.columns:
    if(df[column].dtype!=object):
        print("Maximum value of column",column,":",df[column].max())
        print("Minimum value of column",column,":",df[column].min())
        print("Range of column",column,":",df[column].max()-df[column].min())
        print("#############################################################")
##########################################################################################################
#Q12
print("IQR of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        q1, q3= np.percentile(df[column],[25,75])
        iqr = q3 - q1
        lower_bound = q1 -(1.5 * iqr) 
        upper_bound = q3 +(1.5 * iqr) 
        print("Interquartile range of column",column,":",iqr)
        print("Lower bound of column ",column,":",lower_bound)
        print("Upper bound of column ",column,";",upper_bound)
        outlier=[]
        for i in (df[column]):
          if lower_bound<i and i>upper_bound:
               outlier.append(i)
        print("Outliers are:",outlier)
        if not outlier:
          print("No Outlier Present")
        print("###############################################")
             