# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:07:30 2019

@author: Siddharth Singh
"""

import re
valid=[]
while True:
    n=input("enter the email: ")
    if not n:
        break
    elif re.fullmatch(r'[a-z\_\-0-9]+@[a-zA-Z]+\.[a-z]{2,4}',n):
        valid.append(n)
    else:
        print(False)
print(valid)   



