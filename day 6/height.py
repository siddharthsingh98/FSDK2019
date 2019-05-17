# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:47:42 2019

@author: Siddharth Singh
"""
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
print(type(people))
height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)




from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

def f(x):
    if 'height' in x:
        return x

def add(y):
    height_total=0
    height_total+=y['height']
    return height_total
def add1(z):
    height_count=0
    height_count+=1
    return height_count
def total(x,y):
    return x+y
g =filter(f,people)
result=list(map(add,filter(f,people)))
result1=list(map(add1,filter(f,people)))
s1=reduce(total,result)
s2=reduce(total,result1)
print('average heinght= ',s1/s2)

#code by sir
def people_h(x):
    return "height" in x

def find_h(x):
    return x["height"]

def add(x,y):
    return x+y

heights = list(map(find_h,filter(people_h,people)))

if len(heights) > 0:
    print(reduce(add,heights)/len(heights))



