# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:11:37 2019

@author: Siddharth Singh
"""

from pandas import DataFrame as df
import requests
from selenium import webdriver
import sqlite3
conn= sqlite3.connect('empoyee.db')
c=conn.cousor()
crick="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

chrome=webdriver.Chrome(r"D:\forsk\day 8\chromedriver.exe")
a=chrome.get(crick)

a=[]
b=[]
c=[]
d=[]

for i in range(1,11):
    w=chrome.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[1]')
    x=chrome.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[2]')
    y=chrome.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[3]')
    z=chrome.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[4]')
    a.append(w.text)
    b.append(x.text)
    c.append(y.text)
    d.append(z.text)
print(a)
print(b)
print(c)
print(d)

c.execute("""crete table teams(
        rank INTEGER,
        country TEXT,
        matches INTEGER,
        points INTEGER))
          """)

C.execute("INSERT INTO students VALUES ('a',15,01,'cs')")
C.execute("INSERT INTO students VALUES ('b',15,02,'civil')")
C.execute("INSERT INTO students VALUES ('c',15,03,'mech')")
C.execute("INSERT INTO students VALUES ('d',15,04,'cs')")
C.execute("INSERT INTO students VALUES ('e',15,05,'it')")
C.execute("INSERT INTO students VALUES ('f',15,06,'civil')")
C.execute("INSERT INTO students VALUES ('g',15,07,'cs')")
C.execute("INSERT INTO students VALUES ('h',15,09,'ec')")
C.execute("INSERT INTO students VALUES ('i',15,10,'ee')")
