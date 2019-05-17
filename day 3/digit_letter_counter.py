# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:42:24 2019

@author: Siddharth Singh
"""

string1=input("enter the string:")
d1=dict()
print(string1)
letters=0
digits=0
print(type(string1))
for item in string1:
    if item.isalpha():
        letters+=1
    elif item.isdigit():
        digits+=1
print("letters= ",letters)
print("digits= ",digits)

d1["letters"]=letters
d1["digits"]=digits
print(d1)