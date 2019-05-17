# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:11:06 2019

@author: Siddharth Singh
"""

str=input("enter your name")#takes the string input from the user
print(str[::-1]) #print the string in reverse order
print(" ".join(str))#add the spaces in the string
#reverse the added spaced string
print(" ".join(str[::-1])) 