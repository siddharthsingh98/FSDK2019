# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:50:09 2019

@author: Siddharth Singh
"""
import requests

url1="http://api.openweathermap.org/data/2.5/weather"
url2="?q="+input("enter the city you want the information of: ")
url3="&appid=e9185b28e9969fb7a300801eb026de9c"

url=url1+url2+url3

response=requests.get(url)

print(response.content) 
print("status code= "+str(response.status_code))

jsondata=response.json()
print(type(jsondata))
print(jsondata)
print(jsondata["coord"])
print(jsondata["weather"])


