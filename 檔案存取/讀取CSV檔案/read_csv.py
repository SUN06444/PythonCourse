# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:07:37 2018

@author: Student
"""

import csv

fn = 'C:/Users/Student/practice0526.csv'

with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)
print(listReport)