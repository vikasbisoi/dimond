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
from tkinter import *
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



 
def UploadAction(event=None):
    path = filedialog.askopenfilename()
    print('Selected:', path )
    global df
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
button = tk.Button(root, text='Open Dataset', command=UploadAction)
button.pack()

root.mainloop()

#==============================================================================
"""
Reading Data
read_csv() is the function in pandas which reads csv files.
head() function is used to print first five rows of dataset.
(default number of rows is 5)
"""
#df= pd.read_csv ("diamonds-m.csv")
df.head()
#==============================================================================

'''def UploadAction(event=None):
    """The function takes the location from the user and prints the first five
    rows of the dataset.
    """
    path = filedialog.askopenfilename()
    print('Selected:', path )
    global df
    if path.endswith(".csv"):
        df= pd.read_csv(path)
        print(df.head())
    elif path.endswith(".xlsx"):
        df= pd.read_excel(path)
        print(df.head())
    elif path.endswith(".txt"):
        df= pd.read(path)
        print(df.head())
    #return df
root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()
#root.after(5000, root.destroy)
root.mainloop()'''
###############################################################################
from tkinter import *
master = Tk()

def run_all():
    var1.set(1)
    var2.set(1)
    var3.set(1)
    var4.set(1)
    var5.set(1)
    var6.set(1)
    var7.set(1)
    var8.set(1)
    var9.set(1)
    var10.set(1)
    var11.set(1)
    var12.set(1)
    var13.set(1)
    var14.set(1)
    var15.set(1)
    var16.set(1)
    var17.set(1)
    var18.set(1)
    Q1()
    Q2()
    Q3()
    Q4()
    Q5()
    Q6()
    Q7()
    Q8()
    Q9()
    Q10()
    Q11()
    Q12()
    Q13()
    Q14()
    Q15()
    Q16()
    Q17()
    Q18()
    
    master.destroy()

def Q1():
    if(var1.get()==1):
        print("==============================================================")
        print("The Strucure of the dataset is:",shape_of_dataset(df))
        print("==============================================================")
def Q2():
    if(var2.get()==1):
        print("==============================================================")
        print("The Datatypes of each column is as follows:")
        print(data_types(df))
        print("==============================================================")

       
def Q3():
    if(var3.get()==1):
        print("==============================================================")
        print("The length of the alphanumeric columns are is follows:")
        print(data_types(df))
        print("==============================================================")

def Q4():
    if(var4.get()==1):
        print("==============================================================")
        for column in list(df.select_dtypes(include='float64').columns):
            print(column)
            new_list = []
            for x in range(len(df[column])-1):
                if not math.isnan(df[column][x]):
                    new_list.append(precision_and_scale(df[column][x]))
            print(set(new_list))
        print("==============================================================")
def Q5():
    if(var5.get()==1):
        print("==============================================================")
        print("The Significant columns of the dataset are as follows:")
        print(significant(list(df.columns)))
        print("==============================================================")

def Q6():
    if(var6.get()==1):
        print("==============================================================")
        print("Number of null values in each column of the dataset are as follows:")
        print(nullvalues(df))
        print("--------------------------------------------------------------")
        print("Number of Zero values in each column of the dataset are as follows:")
        print(zerovalues(df))
        print("==============================================================")
        
def Q7():
    if(var7.get()==1):
        print("==============================================================")
        print("We can observe the Obvious Errors of the dataset from below:")
        obvious_errors(df)
        print("==============================================================")

def Q8():
    if(var8.get()==1):
        print("==============================================================")
        replace_null(df)
        print("==============================================================")

def Q9():
    if(var9.get()==1):
        print("==============================================================")
        print("If we replace any value with zero,The summary of  dataset will be distributed.")
        print("==============================================================")

def Q10():
    if(var10.get()==1):
        print("==============================================================")
        print("Quartile summary along with the count , mean & sum of the dataset is as follows:")
        quartile_summary(df)
        print("==============================================================")
        

def Q11():
    if(var11.get()==1):
        print("==============================================================")
        print(" range, variance and standard deviation of the dataset is as follows:")
        range_variance_sd(df)
        print("==============================================================")

def Q12():
    if(var12.get()==1):
        print("==============================================================")
        print(" Count of outliers and their value of the dataset is as follows:")
        Outlierss(df)
        print("==============================================================")

def Q13():
    if(var13.get()==1):
        print("==============================================================")
        print("Class and categoric variable")
        classandcategoric(df) 
        print("==============================================================")
 
def Q14():
    if(var14.get()==1):
        print("==============================================================")
        print("box & whisker plot:")
        histogram(df)
        print("==============================================================")

def Q15():
    if(var15.get()==1):
        print("==============================================================")
        print("Histogram:")
        boxplot(df)
        print("==============================================================")
        
def Q16():
    if(var16.get()==1):
        print("==============================================================")
        print("correlation table & graph:")
        corrletion(df)
        print("==============================================================")

def Q17():
    if(var17.get()==1):
        print("==============================================================")
        print("relationship chart showing relation of each numeric column with all other numeric columns:")
        relationship(df)
        print("==============================================================")

def Q18():
    if(var18.get()==1):
        print("==============================================================")
        print("difference between the Actual Depth & Ideal Depth:")
        actual_ideal(df)
        print("==============================================================")
                                

Label(master, text="Choose Questions:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Question 1", variable=var1,command=Q1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Question 2", variable=var2,command=Q2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Question 3", variable=var3,command=Q3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Question 4", variable=var4,command=Q4).grid(row=4, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Question 5", variable=var5,command=Q5).grid(row=5, sticky=W)
var6 = IntVar()
Checkbutton(master, text="Question 6", variable=var6,command=Q6).grid(row=6, sticky=W)
var7 = IntVar()
Checkbutton(master, text="Question 7", variable=var7,command=Q7).grid(row=7, sticky=W)
var8 = IntVar()
Checkbutton(master, text="Question 8", variable=var8,command=Q8).grid(row=8, sticky=W)
var9 = IntVar()
Checkbutton(master, text="Question 9", variable=var9,command=Q9).grid(row=9, sticky=W)
var10 = IntVar()
Checkbutton(master, text="Question 10", variable=var10,command=Q10).grid(row=10, sticky=W)
var11 = IntVar()
Checkbutton(master, text="Question 11", variable=var11,command=Q11).grid(row=11, sticky=W)
var12 = IntVar()
Checkbutton(master, text="Question 12", variable=var12,command=Q12).grid(row=12, sticky=W)
var13 = IntVar()
Checkbutton(master, text="Question 13", variable=var13,command=Q13).grid(row=13, sticky=W)
var14 = IntVar()
Checkbutton(master, text="Question 14", variable=var14,command=Q14).grid(row=14, sticky=W)
var15 = IntVar()
Checkbutton(master, text="Question 15", variable=var15,command=Q15).grid(row=15, sticky=W)
var16 = IntVar()
Checkbutton(master, text="Question 16", variable=var16,command=Q16).grid(row=16, sticky=W)
var17 = IntVar()
Checkbutton(master, text="Question 17", variable=var17,command=Q17).grid(row=17, sticky=W)
var18 = IntVar()
Checkbutton(master, text="Question 18", variable=var18,command=Q18).grid(row=18, sticky=W)

Button(master, text='Run all', command=run_all).grid(row=19, sticky=W, pady=4)
mainloop()
###############################################################################
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
    print(set(new_list))

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
    
______________________________________________________________________________
If we replace any value with zero,The summary of  dataset will be distributed.
______________________________________________________________________________

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
            print("-------------------------------------------------------------------")
    print("----------------------------------------------------------------------") 
rvs=range_variance_sd(df)


#==============================================================================

"""
12. For each numeric column
▪ Provide the count of outliers and their value
"""
def Outlierss(dataset):
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
                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
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
                print("----------------------------------------------------------")
Outlierss(df)
#=============================================================================
"""
13. Are there any class or categoric variables? If yes ,
▪ provide frequency distribution table & chart for the same
"""

def classandcategoric(dataset):
    column_name= []
    for column in list (df.columns):
        if df[column].dtype == 'object':
            column_name.append(column)
            print(column)
    df_new= df[column_name]
    print(df_new.head())
    for i in df_new:
        plt.figure(figsize=(20,10))
        df_new.loc[:,i].hist()
        plt.show()
    
classandcategoric(df)        


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
