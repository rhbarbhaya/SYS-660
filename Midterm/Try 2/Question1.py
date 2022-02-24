# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:22:21 2019

@author: rhbar
"""

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.stats as stats

percent = pd.read_csv("percent.csv")
oldcars = pd.read_csv("oldcars.csv")
newcars = pd.read_csv("newcars.csv")

# =============================================================================
# r1 = np.random.uniform(1,1000)
# per = percent.iat[0,0]
# pro = r1*per
# miles = oldcars.iat[0,1] * pro
# print (miles)    
# =============================================================================

rangs = []
muls = []
total_miles_old = []
year0 = percent(["Year0","Year1"])#iloc[:,2]
upper = percent.iloc[:,0]
lower = percent.iloc[:,1]
oldcar_no = oldcars["No of cars"]#.iloc[:,:2]
oldcar_no_1 = oldcar_no[0]
oldcar_no_1_1= []

for j in year0:
    oldcar_miles = oldcar_no*j
    oldcar_no_1_1.append(oldcar_miles)


# =============================================================================
# for i in range(11):
#     u = np.random.uniform(lower[i], upper[i])
#     rangs.append(u)
#     
# for i in range(11):
#     mul = rangs[i] * year0[i]
#     muls.append(mul)
#     
# for i in oldcar[:,1]:
#     for j in muls:
#         miles0 = i*j
#         total_miles_old.append([miles0])
# =============================================================================
        
