# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:10:33 2019

@author: Siddharth Singh
"""
import re

N=input("enter the floating number")
if re.fullmatch(r'\+?\-?\.?[0-9]*\.[0-9]*',N):
    print(True)
else:
    print(False)