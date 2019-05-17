# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:26:44 2019

@author: Siddharth Singh
"""
from collections import OrderedDict

od=OrderedDict()

while True:
    inp=input()
    if not inp:
        break
    inp=inp.split()
    k=' '.join(inp[:-1])
    if k in od.keys():
        od[k]+=int(inp[-1])
    else:
        od[k]=int(inp[-1])
        
#
d1={}
for i in range():
    d1[input("enter key"+str(i)+" ")]=int(input("enter val"+str(i)+" "))




