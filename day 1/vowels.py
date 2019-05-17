# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:48:49 2019

@author: Siddharth Singh
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels = ['a','e','i','o','u']
new = []
for state in state_name:
    list1=list(state.lower())
    print(list1)
    for vowel in vowels:
        while vowel in list1:
            list1.remove(vowel)
            print("".join(list1))
    new.append("".join(list1))
    print(new)