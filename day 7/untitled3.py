# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:36:02 2019

@author: Siddharth Singh
"""

import requests

url1="https://free.currconv.com/api/v7/convert"
url2="?q=USD_INR&compact=ultra"
url3="&apiKey=a8e2d8d9dc6274a6c67f"

url=url1+url2+url3

response=requests.get(url)
print(response.content)
