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
tkinter GUI library.
"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import math
#==============================================================================
"""
Setting Maximum option for columns to see all the columns in outputs.
"""
pd.set_option("display.max_columns",None)

#==============================================================================
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
Applying conditions where data file with specific extension can be open 
or print. 
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


 
def UploadAction(event=None):
    path = filedialog.askopenfilename()
    print('Selected:', path )
    if path.endswith(".csv"):
        df= pd.read_csv(path) 
        print(df.head())
    elif path.endswith(".xlsx"):
        df= pd.read_excel(path) 
        print(df.head())
    elif path.endswith(".txt"):
        df= pd.read(path) 
        print(df.head())

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()

    
#==============================================================================
"""
Reading Data
read_csv() is the function in pandas which reads csv files.
head() function is used to print first five rows of dataset.
(default number of rows is 5)
"""
df= pd.read_csv ("diamonds-m.csv")
df.head()

#==============================================================================
"""
1. What is structure of the dataset.
shape () function returs the number of rows and columns in dataset.
"""
def shape_of_dataset(dataset):
    """The Function returns the shape of the dataset
    i.e the structure of dataset"""
    sh=dataset.shape
    return sh
shape=shape_of_dataset(df)
print("The Strucure of the dataset is:",shape)    

#==============================================================================
"""
2 . What are the data type of each columns?
dtypes is the function in python which returns the data types of 
all thr columns in the dataset.
"""
#print(df.dtypes)

def data_types(dataset):
    """The Functions returns the data type of the columns """
    dt=dataset.dtypes
    return dt
datatype=data_types(df)
print(datatype)

#=====================================================================================

"""
3 . What is the length of alpha numeric columns ?
"""

def alpha_numeric_columns(dataset):
    """The functions returns the length of alpha numeric 
    columns"""
    for column in dataset.columns:
        if dataset[column].dtype == 'object':
            print(column ,": ", dataset[column].str.len().max())
alphanum=alpha_numeric_columns(df)

#=============================================================================

"""
4 . What are precision & scale of numeric columns?
"""

def precision_and_scale(x):
    """The functions returns the precision and scale of 
    numeric columns"""
    max_digits = 14
    int_part = int(abs(x))
    magnitude = 1 if int_part == 0 else int(math.log10(int_part)) + 1
    if magnitude >= max_digits:
        return (magnitude, 0)
    frac_part = abs(x) - int_part
    multiplier = 10 ** (max_digits - magnitude)
    frac_digits = multiplier + int(multiplier * frac_part + 0.5)
    while frac_digits % 10 == 0:
        frac_digits /= 10
    scale = int(math.log10(frac_digits))
    return (magnitude + scale, scale)

for column in list(df.select_dtypes(include='float64').columns):
    print(column)
    new_list = []
    for x in range(len(df[column])-1):
        if not math.isnan(df[column][x]):
            new_list.append(precision_and_scale(df[column][x]))
    print(new_list)

#==============================================================================
"""
5 . Identify significant columns of the data set .
"""

def significant(a):
    """The function return the number of significant columns """
    for i in  a:
#    print(i)
        if i=="id":
            a.remove("id")
            return(a)
#a=list(df.columns)
d=significant(list(df.columns))
print("The list of significant columns are :",d)
#==============================================================================
"""
6 . For each column, find out
▪ Number of Null values
▪ Number of zeros
"""
def nullvalues(dataset):
    """The function returns the number of null values """
    nl=dataset.isnull().sum()
    return nl
null=nullvalues(df)
print(null)    

def zerovalues(dataset):
    """The function returns the number of zeros in dataset  """
    ze=dataset.isin([0]).sum()
    return ze
zero=zerovalues(df)
print(zero)
#==============================================================================

"""
7 . For each column
▪ Provide the obvious errors
"""

def obvious_errors(dataset):
    """The functions prints the uniques values for each column."""
    pd.options.display.float_format = '{:,.2f}'.format
    for colName in df.columns:
        if  df[colName].dtype == 'object':
            print("Unique values in",colName,"\n",df[colName].unique()) 
oe=obvious_errors(df)

#==============================================================================
"""
8 . For each numeric column
▪ Replace null values with median value of the column .
"""

def replace_null(dataset):
    """The function replace's the null values by median for all numeric 
    columns"""
    for column in df.columns:
        if df[column].dtype!=object:
            if column!='id':
                print("number of null vallues in column",column,":",
                      df[column].isnull().sum())
                df[column]=df[column].fillna(df[column].median())
                print("number of null vallues in column",column," after replacing it with median:",df[column].isnull().sum())
                print("------------------------------------------------------------")
rn=replace_null(df)

#==============================================================================
"""
9 . For each numeric column
▪ Replace zero values with suitable statistical value of the column . \
    Give reason why
"""


#==============================================================================
"""
10. For each numeric column
▪ Provide the quartile summary along with the cout , mean & sum
"""
def quartile_summary(dataset):
    """The function returns the quartile summary along with count,mean 
    and sum for all numeric columns"""
    print("Mean of all the numeric columns:")
    for column in dataset.columns:
        if(dataset[column].dtype!=object):
            print(column,":",dataset[column].mean())
    print("-----------------------------------------") 
    print("Count of all the numeric columns:")
    for column in dataset.columns:
        if(dataset[column].dtype!=object):
            print(column,":",dataset[column].count())
    print("-----------------------------------------")    
    print("Sum of all the numeric columns:")
    for column in dataset.columns:
        if(dataset[column].dtype!=object):
            print(column,":",dataset[column].sum())
    print("-----------------------------------------")    
    print("The quartile summary of each column are:")
    print(dataset.quantile([0.25,0.50,0.75]))
qs=quartile_summary(df)

#==============================================================================

"""
11. For each numeric column
▪ Provide the range, variance and standard deviation
"""

def range_variance_sd(dataset):
    """the function prints the Range,Variance and Standar deviatation for 
    all numeric columns"""
    print("variance of all the numeric columns:")
    for column in df.columns:
        if(df[column].dtype!=object):
            print(column,":",df[column].var())       
    print("----------------------------------------------------------------------")
    print("Standard deviation of all the numeric columns:")
    for column in df.columns:
        if(df[column].dtype!=object):
            print(column,":",df[column].std())
    print("----------------------------------------------------------------------")        
    for column in df.columns:
        if(df[column].dtype!=object):
            print("Maximum value of column",column,":",df[column].max())
            print("Minimum value of column",column,":",df[column].min())
            print("Range of column",column,":",df[column].max()-df[column].min())
    print("----------------------------------------------------------------------") 
rvs=range_variance_sd(df)


#==============================================================================

"""
12. For each numeric column
▪ Provide the count of outliers and their value
"""
def outliers(dataset):
    """The function prints the count of outlier and their values """
    print("IQR of all the numeric columns:")
    for column in dataset.columns:
        if(dataset[column].dtype!=object):
            q1, q3= np.percentile(dataset[column],[25,75])
            iqr = q3 - q1
            lower_bound = q1 -(1.5 * iqr)
            upper_bound = q3 +(1.5 * iqr)
            print("Interquartile range of column",column,":",iqr)
            print("Lower bound of column ",column,":",lower_bound)
            print("Upper bound of column ",column,":",upper_bound)
            outlier=[]
            for i in (dataset[column]):
                if lower_bound<i>upper_bound:
                    outlier.append(i)
            print("Outliers are:",outlier)
            if not outlier:
                print("No Outlier Present")
            print("--------------------------------------------------------------")
ot=outliers(df)
#=============================================================================
"""
13. Are there any class or categoric variables? If yes ,
▪ provide frequency distribution table & chart for the same
"""


#=============================================================================

"""
14. For all numeric columns
▪ Provide histogram
"""
def histogram(dataset):
    """The function returns the histogram for all numeric columns """
    plt.figure(figsize=(10,10))
    dataset.hist(sharey=True,align="mid")
    plt.tight_layout()
    return plt.show()
ht=histogram(df)

#==============================================================================

"""
15. For all numeric variables
▪ Provide box & whisker plot
"""
def boxplot(dataset):
    """The function returns the box and whisker plot for all numeric
    columns  """
    plt.figure()
    sb.boxplot(data=dataset,orient="h")
    return plt.show()
bx=boxplot(df)

#==============================================================================
"""
16. For all numeric variables
▪ Provide correlation table & graph
"""
def corrletion(dataset):
    """The functions returns the correlation and graph for all numeric 
    columns """
    corr=dataset.corr()
    print(corr)
    plt.figure()
    sb.heatmap(corr,vmax=1,annot=True,linecolor="black",linewidth=0.5)
    return plt.show()
cr=corrletion(df)

#==============================================================================
"""
17. Prepare relationship chart showing relation of each numeric
column with all other numeric columns .
"""
def relationship(dataset):
    """The function returns the Relationship chart for all numerical values. """
    plt.figure()
    sb.pairplot(dataset)
    return plt.show()
rs=relationship(df)

#==============================================================================
"""
18. Find out the difference between the Actual Depth & Ideal Depth .
"""
def actual_ideal(dataset):
    """The functions prints the difference between the actual depth and 
    ideal depth"""
    m=(np.mean(dataset.x)+np.mean(dataset.y))/2
    dataset["ideal_depth"]=dataset.z/m
    dataset["Difference"]=dataset["depth"]-dataset["ideal_depth"]
    print(dataset["Difference"])
ai=actual_ideal(df)
