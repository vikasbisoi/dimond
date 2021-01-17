# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:59:54 2021

@author: SIDDHESH
"""
"""
Importing Libraries.
Pandas for reading data files.
Numpy for calculating statistical values.
Seaborn and Matplotlib for data visualization.
"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
#======================================================================================
"""
Setting Maximum option for columns to see all the columns in outputs.
"""
pd.set_option("display.max_columns",None)

#======================================================================================
"""
Taking input from user.
Asking user to give loction of data file with extension.
After getting location relpacing forslash to backward slash 
"""

#C:\Users\SIDDHESH\OneDrive\Desktop\R.J clg\Project_cyrussir\CPW\diamonds-m.csv
path=input("Enter The Path of your dataset with extension:")
path=path.replace("\\","/")
#print(str(path))
"""
Applying conditions where data file with specific extension can be open or print. 
"""
if path.endswith(".csv"):
    df= pd.read_csv(path) 
    print(df.head())
elif path.endswith(".xlsx"):
    df= pd.read_excel(path) 
    print(df.head())
elif path.endswith(".txt"):
    df= pd.read(path) 
    print(df.head())




    
#======================================================================================
"""
Reading Data
read_csv() is the function in pandas which reads csv files.
head() function is used to print first five rows of dataset.(default number of rows is 5)
"""
df= pd.read_csv ("diamonds-m.csv")
df.head()

#=====================================================================================
"""
1. What is structure of the dataset.

shape () function returs the number of rows and columns in dataset.
"""
print("The Strucure of the dataset is:",df.shape)

#=====================================================================================
#Output
#The Strucure of the dataset is: (53940, 12)

#=====================================================================================
"""
2 . What are the data type of each columns?

dtypes is the function in python which returns the data types of all thr columns in the 
dataset.
"""
print(df.dtypes)

#=====================================================================================
#Output
#   Column      Data types 
#   id              int64
#   carat         float64
#   cut            object
#   color          object
#   clarity        object
#   popularity     object
#   depth         float64
#   table         float64
#   price         float64
#   x             float64
#   y             float64
#   z             float64
#=====================================================================================

"""
3 . What is the length of alpha numeric columns ?


"""
df.columns

df["cut_alp"]=map(lambda x: x.isalnum(),df["cut"] ).sum()
print(df["cut_alp"])


df["clarity_alp"]=map(lambda x: x.isalnum(),df["clarity"] )
print(df)


print(len(df["clarity"].str.isalnum()))

df["cut"].unique()
df["cut"].str.isalnum()

df["color"].unique()
df["color"].str.isalnum()

df["popularity"].unique()
df["popularity"].str.isalnum()

df["clarity"].unique()
df["clarity"].str.isalnum()
#alpha=df["carat"].astype(str).str.isalnum()
#print(len(alpha))





#==============================================================================

"""
4 . What are precision & scale of numeric columns?
"""






#==============================================================================
"""
5 . Identify significant columns of the data set .
"""

def significant(a):
    for i in  a:
#    print(i)
        if i=="id":
            a.remove("id")
            return(a)
#a=list(df.columns)
d=significant(list(df.columns))
print("The list of significant is :",d)

#==============================================================================
"""
6 . For each column, find out
▪ Number of Null values
▪ Number of zeros
"""


