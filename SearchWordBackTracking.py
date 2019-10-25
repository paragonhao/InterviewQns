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

backTrack = np.zeros((maxRows,maxCols))

word = ["A", "B", "C", "D","I"]
wordLen = len(word)

path = 1

def SearchWord(count, i, j):
    
    if backTrack[i][j] != 0 or word[count] != mat[i][j]:
        return False
    
    if count == (wordLen - 1):
        backTrack[i][j] = 1
        return True
    
    backTrack[i][j] = 1 
    
    if ((i + 1) < maxRows) and SearchWord(count+1, i + 1, j):
        return True
        
    if ((i - 1) >= 0) and SearchWord(count+1, i - 1, j):
        return True
        
    if ((j + 1) < maxCols) and SearchWord(count+1, i, j+1):
        return True
    
    if ((j - 1) >= 0) and SearchWord(count+1, i, j-1):
        return True
    
    return False

def Search():
    
    for i in range(maxRows):
        for j in range(maxCols):
            if SearchWord(0, i, j):
                return True
    return False

if Search():
    print("Found")
else:
    print("Not Found")