# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:57:04 2019

@author: Siddharth Singh
"""
start=int(input("enter the no it iteration"))
for value in range(0,start+1):
    print("* "*value)
    if (start == value):
        for item in range(start-1,0,-1):
            print("* "*item)