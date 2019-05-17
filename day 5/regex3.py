# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:57:33 2019

@author: Siddharth Singh
"""
import re
while True:
    card=input("enter the card no: ")
    if not card:
        print("not entered any input")
        break
    if re.match(r'^[[456]([0-9]{15}|[0-9]{3}(-[0-9]{4}){2}-([0-9]{4}))',card):
        q=re.match(r'^[[456]([0-9]{15}|[0-9]{3}(-[0-9]{4}){2}-([0-9]{4}))',card)
        r=re.match(r'(0-9)\1{2,4}',card)
        if r==q:
            print("not valid")
            break
        print("valid")
    else:
        print("not_valid")
        