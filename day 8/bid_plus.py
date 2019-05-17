# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:36:12 2019

@author: Siddharth Singh
"""

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
from collections import OrderedDict as od

web_page="https://bidplus.gem.gov.in/bidlists"

driver=webdriver.Chrome(r"D:\forsk\day 8\chromedriver.exe")

a=driver.get(web_page)
a=[]
b=[]
c=[]
d=[]
sleep(2)
for i in range(1,11):
    get_bid_pdf = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    get_bid_pdf1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    get_bid_pdf2 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    get_bid_pdf3 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    a.append(get_bid_pdf.text)
    b.append(get_bid_pdf1.text)
    c.append(get_bid_pdf2.text)
    d.append(get_bid_pdf3.text)
    
print("BID_NO: ",a,"\n\n")
print("item: ",b,"\n\n")
print("Quantity_Required: ",c,"\n\n")
print("Department Name And Address: ",d,"\n\n")

lname=["BID_NO:","item:","Quantity_Required:","Department Name And Address:"]
ldata=od(zip(lname,[a,b,c,d]))
df=pd.DataFrame(ldata)
print(df)
df.to_csv(r"D:\forsk\day 8\bidplus.csv",index=True,header=True)
