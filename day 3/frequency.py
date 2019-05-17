# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:11:21 2019

@author: Siddharth Singh
"""

string=input("enter the stsring")
list1=list(string)
dict1=dict()
print(list1)
for key in string:
    if key in dict1:
        dict1[key]+=1
    else:
        dict1[key]=1
print(dict1)
print(dict1['g'])