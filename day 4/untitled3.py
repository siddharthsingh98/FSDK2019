# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:20:52 2019

@author: Siddharth Singh
"""

import csv
from collections import OrderedDict

groups=OrderedDict()


with open("zoo.csv") as csv_file: 
    csv_reader=csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if row[0] in groups.keys():
            groups[row[0]]=groups[row[0]].append(row[1]),groups[row[0]].append(row[2])
        else:
            groups[row[0]]=groups[row[0]].append(row[1]),groups[row[0]].append(row[2])
            
print(groups)
        
       
        
        
        
        
        
        
        
        
        
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
    