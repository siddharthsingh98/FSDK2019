# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:55:51 2019

@author: Siddharth Singh
"""

import pymongo

client = pymongo.MongoClient("mongodb://sid:sid12345@cluster0-shard-00-00-kl6jl.mongodb.net:27017,cluster0-shard-00-01-kl6jl.mongodb.net:27017,cluster0-shard-00-02-kl6jl.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.dbfirst

def add_employee(idd, first, last, pay):
    mydb.collect.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.collect.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', 50000)
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()

