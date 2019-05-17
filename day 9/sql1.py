# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:07:15 2019

@author: Siddharth Singh
"""

import os
from pandas import DataFrame as df 
import sqlite3

conn = sqlite3.connect('employee.db')

C = conn.cursor()

C.execute("""create table students(
        name TEXT,
        age INTEGER,
        ROLL_NO INTEGER,
        BRANCH TEXT)
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

a=C.execute("SELECT * from students")

print(C.fetchone())
print(C.fetchall())
print(df(C.fetchall()))
C.execute("DROP table students")

df.C.execute("SELECT * from students")
conn.commit()
conn.close()

for i in range(1,10):
    C.execute("INSERT INTO students VALUES ('a',15,01,'cs')")
