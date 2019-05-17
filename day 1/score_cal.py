# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:48:15 2019

@author: Siddharth Singh
"""

print("assigments")
A1=int(input("enter the assigment 1 marks"))
A2=int(input("enter the assigment 2 marks"))
A3=int(input("enter the assigment 3 marks"))
print("exams")
E1=int(input("enter the exam1 marks"))
E2=int(input("enter the exam2 marks"))
weighted_score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
print(weighted_score)