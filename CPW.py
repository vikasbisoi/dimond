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
import networkx as nx
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

for column in df.columns:
    if df[column].dtype == 'object':
        print(column ,": ", df[column].str.len().max())
#=============================================================================
#optional

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
#Output
#The list of significant columns are :
#['carat', 'cut', 'color', 'clarity', 'popularity', 'depth', 'table', 'price',
# 'x', 'y', 'z']
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
#=============================================================================
#Output
#Columns  No. of Null values
#id             0
#carat          2
#cut            0
#color          3
#clarity        0
#popularity    10
#depth          0
#table          0
#price          4
#x              0
#y              0
#z              0
#==============================================================================

def zerovalues(dataset):
    """The function returns the number of zeros in dataset  """
    ze=dataset.isin([0]).sum()
    return ze
zero=zerovalues(df)
print(zero)
#==============================================================================
#columns    No. of zeros in dataset
#id             0
#carat          0
#cut            0
#color          0
#clarity        0
#popularity     0
#depth          0
#table          0
#price          0
#x              8
#y              7
#z             20
#==============================================================================


##Optional
def nullzero(dataset):
    """The function returns the number of zeros in dataset  """
    nl=dataset.isnull().sum()
    #nl=pd.DataFrame(nl)
    ze=dataset.isin([0]).sum()
    #ze=pd.DataFrame(ze)
    return nl,ze
zero=nullzero(df)
zero=pd.DataFrame(zero)
values=["Null","Zeros"]
zero["values"]=values
print(zero.set_index("values"))
#==============================================================================
#Output
#        id  carat  cut  color  clarity  popularity  depth  table  price  x  y   z
#values                                                                          
#Null     0      2    0      3        0          10      0      0      4  0  0   0
#Zeros    0      0    0      0        0           0      0      0      0  8  7   20
#==============================================================================

"""
7 . For each column
▪ Provide the obvious errors
"""
s=[]
for i in  df.columns:
    if (df.columns).dtype==object:
        s.append(i) 
print(s)    
    
    
    
    
grp=df.count()
grp
#==============================================================================
"""
8 . For each numeric column
▪ Replace null values with median value of the column .
"""
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


#==============================================================================
"""
9 . For each numeric column
▪ Replace zero values with suitable statistical value of the column . \
    Give reason why
"""


#==============================================================================
#Q10
"""
10. For each numeric column
▪ Provide the quartile summary along with the cout , mean & sum
"""
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

#==============================================================================
#Q11
"""
11. For each numeric column
▪ Provide the range, variance and standard deviation
"""
print("variance of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].var())
        
print("======================================================================")
print("Standard deviation of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        print(column,":",df[column].std())
print("======================================================================")        
for column in df.columns:
    if(df[column].dtype!=object):
        print("Maximum value of column",column,":",df[column].max())
        print("Minimum value of column",column,":",df[column].min())
        print("Range of column",column,":",df[column].max()-df[column].min())
print("======================================================================") 



#==============================================================================
#Q12
"""
12. For each numeric column
▪ Provide the count of outliers and their value
"""
print("IQR of all the numeric columns:")
for column in df.columns:
    if(df[column].dtype!=object):
        q1, q3= np.percentile(df[column],[25,75])
        iqr = q3 - q1
        lower_bound = q1 -(1.5 * iqr)
        upper_bound = q3 +(1.5 * iqr)
        print("Interquartile range of column",column,":",iqr)
        print("Lower bound of column ",column,":",lower_bound)
        print("Upper bound of column ",column,":",upper_bound)
        outlier=[]
        for i in (df[column]):
          if lower_bound<i>upper_bound:
               outlier.append(i)
        print("Outliers are:",outlier)
        if not outlier:
          print("No Outlier Present")
        print("###############################################")
             
df.head()


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

plt.figure(figsize=(10,10))
df.hist(sharey=True,align="mid")
plt.tight_layout()
plt.show()


#==============================================================================

"""
15. For all numeric variables
▪ Provide box & whisker plot
"""
plt.figure()
sb.boxplot(data=df,orient="h")
plt.show()


plt.figure()
sb.boxplot(x=df["carat"],data=df)
plt.show()
#==============================================================================
"""
16. For all numeric variables
▪ Provide correlation table & graph
"""
corr=df.corr()
print(corr)
plt.figure()
sb.heatmap(corr,vmax=1,annot=True,linecolor="black",linewidth=0.5)
plt.show()
#==============================================================================
"""
17. Prepare relationship chart showing relation of each numeric
column with all other numeric columns .
"""
#df_relation=corr.astype(int)
#print(df_relation)

r= df[df['Object'] == 53940]
edges = []
for idx, rr in r.iterrows():  
        edges.append((rr['Object'], rr['AttributeName']))
print(edges)
#edges=df.columns
g=nx.DiGraph()
g.add_edges_from((edges))
plt.figure()
nx.draw(g,with_labels=True,node_size=5000,font_size=10)
plt.show()

#first try
edges=df.columns
g=nx.DiGraph()
g.add_edges_from((edges))
plt.figure()
nx.draw(g,with_labels=True,node_size=20,font_size=10)
plt.show()


df.shape





#Rohit code
# here we create a empty list and append all the numeric columns in it
column_name5 = []
for column in list (df.columns):
    if df[column].dtype == 'float':
        column_name5.append(column)
        print(column)
df_new5 = df[column_name5]
print(df_new5.head())
    

# correalation (heat map)
#draws  heatmap with input as the correlation matrix calculted by(new_df.corr())
 #cmap – a matplotlib colormap name or object.
 #annot – an array of same shape as data which is used to annotate the heatmap.
 # annonate - to add notes to a book or text, giving explanations or comments



plt.figure() 
sb.heatmap(df_new5.corr(),annot=True,cmap='cubehelix_r') 
plt.show()
#==============================================================================

#==============================================================================
"""
18. Find out the difference between the Actual Depth & Ideal Depth .
"""
print(df.head())
# y = width
#z = depth


#(To find the depth percentage
# divide the diamond's physical depth measurement by its width.
# Also, depth is deemed acceptable within a certain range, 
# with any value between 56.5 and 65 percent considered good. However,
# the ideal depth is between 62.9 and 59.5 percent.)




#  For a round diamond, an ideal depth percentage is between 59 and 62.6 
# percent This very nice 1.30-carat round cut, for example, has a depth of 61.8%


Width_of_Diamond = df.iloc[:,10]
print(Width_of_Diamond)
Depth_of_Diamond = df.iloc[:,11]
print(Depth_of_Diamond)


percentage = (Depth_of_Diamond/Width_of_Diamond)*100
print(percentage)



list67 = []
list69 = []
for i in percentage:
    if 56.5<= i <=65:
        list67.append(i)
for j in percentage:
    if 59.5<= j <=62.9:
        list69.append(j)

TA = len(list67)
TI = len(list69)
hh = (TA/df.shape[0])*100
print("Percentage of Actual is :",hh)
tt = (TI/df.shape[0])*100
print("Percentage of ideal is :",tt)




