# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:46:52 2019

@author: Siddharth Singh
"""
file = open('new.txt', mode='wt')

file.write("Now this has one line\n")
file.writelines(["Second Line\n", "Third Line\n"])
print(file)
print(file.name)
with open("new.txt",'rt') as file:
    print(file.read())
file1= open('new1.txt','wt')
print(file1.name)
file1=file
with open("new.txt",'rt') as file1:
    print(file1.read())
    
    
file = open('new.txt', mode='wt')
file1= open('new1.txt','wt')
for item in range(4):
    with open("new.txt",'rt') as file:
    file1=file
    
with open("new.txt",'rt') as file1:
    print(file1.read())
    
