# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:03:49 2019

@author: Siddharth Singh
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    print(i)
    print(range(len(names)))
    names[i] = random.choice(code_names)
print(names)

#new
names = ['Mary', 'Isla', 'Sam',"jijio"]
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

g=map( lambda name : random.choice(code_names),names)
print(list(g))


