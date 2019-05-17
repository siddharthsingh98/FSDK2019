# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:49:57 2019

@author: Siddharth Singh
"""

list=[1,2,3,4,5,6,7,8,9,10]
type(list)
for item in range(0,9):
    print(item)
    
    
#hands on 1
for i in range(1,21):
    if (i%2==0):
        print(i)
        
        
    #hands on 2
def check():    
    year=int(input("Enter year to be checked:"))
    if(year%4==0 and year%100!=0 or year%400==0):
        return "The year is a leap year"
print(check())

#hands on 3
def days_in_month(month):
    month=month.lower()
    list1=['january','febuary','march']
    list2=[31,28,31]
    index=list1.index(month)
    return list2[index]
    
print(days_in_month("january"))
    
