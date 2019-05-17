# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:27:35 2019

@author: Siddharth Singh
"""

sentence=input("enter the sentence")
alphabet='abcdefghijklmnopqrstuvwxyz'
def pangram(sentence):
    length=len(sentence)-sentence.count(' ')
    if (length<26):
        return False
    elif (length>=26):
        for value in alphabet:
            while value not in sentence:
                return False
        return True
    
print(pangram(sentence))




    