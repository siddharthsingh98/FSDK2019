# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:52:20 2019

@author: Siddharth Singh
"""
#to replace the character R with $ in the input string
str=input("enter the string")
print(str[:1]+str[1:].replace("R","$"))