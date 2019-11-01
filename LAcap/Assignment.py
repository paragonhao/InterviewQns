#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:13:38 2019

@author: paragonhao
"""
import pandas as pd
import numpy as np
import re 


raw_data = pd.read_excel("tFunc.xlsx")
single_pairs = []
result = {}



def parseFunction(func):
    func_input = re.findall("(\$\w+)", func)
    return list(set(func_input))



def map_pairs(raw_data, result):
    for idx, row in raw_data.iterrows():
        inputs = parseFunction(row['Function'])
        output = row['Item Name']
        for i in inputs:
            single_pairs.append([i,output])
            result[i]=[]
    return result, single_pairs



def reduce_pairs(result, single_pairs):
    for i in single_pairs:
        result[i[0]].append(i[1])
    return result

   
result, single_pairs = map_pairs(raw_data, result)
result = reduce_pairs(result, single_pairs)

for key, values in result.items():
    for output in values:
        if output in result.keys():
            result[key] = list(set(result[key] + result[output]))


#testcase ='$rssec6bk'
#for i in single_pairs:
#    if i[0] == testcase or i[1] == testcase:
#        print(i)
#        
#result['$gl1ifcst']