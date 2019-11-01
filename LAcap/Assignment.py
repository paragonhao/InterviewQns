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



def build_graph(key, currentKey):
    
    if key not in result.keys():
        return
    
    if key != currentKey:
        result[currentKey] = list(set(result[key] + result[currentKey]))
    
    for i in result[key]:
        build_graph(i, currentKey)
    

   
result, single_pairs = map_pairs(raw_data, result)
result = reduce_pairs(result, single_pairs)

testcase = '$ime7fcst' # 'rssec5'
build_graph(testcase , testcase)
result[testcase]
