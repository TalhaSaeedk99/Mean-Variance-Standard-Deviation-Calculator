#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd

def calculate(*entries):
    entries_ = []
    for entry in entries:
        entries_.append(entry)
    if len(entries_) != 9:
        print("List must contain nine numbers.")
    else:
        matrix = np.array(entries).reshape(3,3)
        mean1 = np.mean(matrix, axis=0).tolist()
        mean2 = np.mean(matrix, axis=1).tolist()
        mean3 = np.mean(matrix.flatten())
        Variance1 = np.var(matrix, axis=0).tolist()
        Variance2 = np.var(matrix, axis=1).tolist()
        Variance3 = np.var(matrix.flatten())
        STD1 = np.std(matrix, axis=0).tolist()
        STD2 = np.std(matrix, axis=1).tolist()
        STD3 = np.std(matrix.flatten())
        min1 = np.min(matrix, axis=0).tolist()
        min2 = np.min(matrix, axis=1).tolist()
        min3 = np.min(matrix.flatten())
        max1 = np.max(matrix, axis=0).tolist()
        max2 = np.max(matrix, axis=1).tolist()
        max3 = np.max(matrix.flatten())
        sum1 = np.sum(matrix, axis=0).tolist()
        sum2 = np.sum(matrix, axis=1).tolist()
        sum3 = np.sum(matrix.flatten())
        Result = {
        'mean': [mean1, mean2, mean3],
        'variance': [Variance1, Variance2, Variance3],
        'standard deviation': [STD1, STD2, STD3],
        'max': [max1, max2, max3],
        'min': [min1, min2, min3],
        'sum': [sum1, sum2, sum3]
        }
        print(Result)


