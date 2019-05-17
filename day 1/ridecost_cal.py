# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:36:46 2019

@author: Siddharth Singh
"""

import math
distance=int(input("enter the distance to the office"))
d= distance*2
dp=int(input("enter the desil price "))
avg=int(input ("enter the car average" ))
fuel=d/avg
total_cost=dp*fuel
print(total_cost)