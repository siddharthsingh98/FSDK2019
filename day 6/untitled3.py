# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:50:06 2019

@author: Siddharth Singh
"""

input_string = input("Enter a list element separated by space ")
list1 = input_string. split()
print(list1)

for item in list1:
    a=item[::-1]
    if item==a:
        print("true")
    else:
        print("false")