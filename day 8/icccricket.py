# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:21:00 2019

@author: Siddharth Singh
"""

from bs4 import BeautifulSoup as bs
import requests
cric="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(cric).text
soup=bs(source,"lxml")
print(soup) 
print(soup.prettify())
all_tables=soup.find_all('table')
print(all_tables)
right_table=soup.find('table',class_="table")
print(right_table)

a=[]
b=[]
c=[]
d=[]
e=[]

for row in right_table.find_all("tr"):
    cells = row.findAll("td")
    if len(cells)==5:    
        a.append(cells[0].text.strip())
        b.append(cells[1].text.strip())
        c.append(cells[2].text.strip())
        d.append(cells[3].text.strip())
        e.append(cells[4].text.strip())
    
import pandas as ps
from collections import OrderedDict as od
col_name=["position","team","matches","points","rating"]
col_data=od(zip(col_name,[a,b,c,d,e]))
df=ps.DataFrame(col_data)
print(df)
