# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:35:00 2019

@author: Siddharth Singh
"""
number=0
with open("absentee.txt","wt") as file:
    while number<=25:
        a=input("enter the ansentes")
        if not a:
            break
        file.write(a+"\n")
with open("absentee.txt","rt") as file:
    print(file.read())

        
    
    