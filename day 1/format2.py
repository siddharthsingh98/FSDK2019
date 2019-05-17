# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:24:04 2019

@author: Siddharth Singh
"""

str="welcome to city jaipur"
str1= str.split()#split() function splits the string into list whenever a space is arrived
print(str1)
#joining the list with the charater where space is present
"""
.join(str) will join the string
.join(list) will join the list 
"""
print("*".join(str1))