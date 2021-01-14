# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:27:32 2021

@author: admin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
pd.set_option("display.max_columns",None)

diamonds = pd.read_csv("C:/Users/admin/Desktop/dimond/diamonds-m.csv")
diamonds.head()


#Q6 For ea ch column, find ou t
# Number o f Null values
# Number o f zeros


## Number o f Null values
print("Number of null values")
print(diamonds.isnull().sum())

## Number o f zeros
print("Numer of zeros values")
print((diamonds==0).sum())


#Q7 For each column Provide the obvious errors

grp=diamonds.groupby("cut").count()
grp
