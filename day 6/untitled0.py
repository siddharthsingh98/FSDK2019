# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:18:17 2019

@author: Siddharth Singh
"""
list0=["Order Number","Book Title","Author","Quantity","Price per Item"]
list1=["34587","Learning Python","Mark Lutz","4","40.95"]
list2=["98762","Programming Python","Mark Lutz","5","56.80"]
list3=["77226","Head First Python","Paul Barry","3","32.95"]
flist=[list1,list2,list3]
x=[]
y=[]
z=[]
a=list0.index("Order Number")
b=list0.index("Quantity")
c=list0.index("Price per Item")
for item in flist:
    for item1 in item:
        if item.index(item1)==a:
            x.append(item1)
        if item.index(item1)==b:
            y.append(float(item1))
        if item.index(item1)==c:
            z.append(float(item1))
        
print(x)
print(y)
print(z)
print(list((y*z for y,z in zip(listy,listz))))


#optimized code by sir
data = [
["34587","Learning Python","Mark Lutz","4","40.95"],
["98762","Programming Python","Mark Lutz","5","56.80"],
["77226","Head First Python","Paul Barry","3","32.95"]
]

list1 = []

for item in data:
    list1.append((item[0], int(item[3])*float(item[4])))
   
        
        