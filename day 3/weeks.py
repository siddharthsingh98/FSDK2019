# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:13:14 2019

@author: Siddharth Singh
"""

original=['monday','tuesday','wednesday','thrusday','friday','saturday']
enter=input("enter you input: ").split()
print(enter)
enter1=[]
for item in original:
    while item not in enter:
        enter.append(item)
    print(enter)        
    