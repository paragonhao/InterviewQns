#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:45:37 2019
@author: paragonhao
"""
import numpy as np

# initialize the matrix 
mat = [["A", "B", "C", "D","I"],
       ["X", "B", "D", "P","N"],
       ["W", "D", "H", "A","I"],
       ["G", "Y", "X", "Z","I"],
       ["A", "E", "F", "C","D"]]

dim = np.shape(mat)
maxRows = dim[0]
maxCols = dim[1]

word = ["P","A","I","N"]
wordLen = len(word)
count = 0 

def SearchWord(count, i, j):
    
    if count == wordLen:
        print("Found the word!")
        return 0
    
    if (i + 1) < maxRows:
        if(word[count] == mat[i+1][j]):
            SearchWord(count+1, i+1, j)
        
    if (i - 1) >= 0:
        if (word[count] == mat[i-1][j]):
            SearchWord(count+1, i-1, j)
        
    if (j + 1) < maxCols:
        if (word[count] == mat[i][j+1]):
            SearchWord(count+1, i, j+1)
    
    if (j - 1) >= 0:
        if (word[count] == mat[i][j-1]):
            SearchWord(count+1, i, j-1)
    
for i in range(maxRows):
    for j in range(maxCols):
        if word[0] == mat[i][j]:
            count = 0
            SearchWord(count+1, i, j)