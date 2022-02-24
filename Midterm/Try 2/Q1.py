# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:17:06 2019

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
ranges = pd.read_csv("Values.csv")
nnc = pd.read_csv("NoNewCars.csv")
noc = pd.read_csv("NoOldCars.csv")

mess = pd.DataFrame()

def random():
    for i in range(11):
        rand = np.random.uniform(ranges.iat[i,1], ranges.iat[i,2])
        mess["Range1"].append(rand)


random()
# =============================================================================
# df = pd.DataFrame()
# df2 = pd.DataFrame()
# #df3 = pd.DataFrame()
# per_labels = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11"]
# 
#   
# for i in range(11):
#     pointer = per_labels[i]
#     random = np.random.uniform(ranges["Lower Limit"], ranges["Upper Limit"])
#     miles0 = noc.iat[i,0] * random
# #    df[pointer].append
# #    sum_row = {col: df[col].sum() for col in df}
# #    df2 = pd.DataFrame(sum_row, index=["Year0"])
#     # df2 = df2.append(pd.DataFrame(df.sum(axis=0),columns=[pointer]).T)
# 
# # =============================================================================
# # for i in range(11):
# #     random = np.random.normal(ranges["Lower Limit"], ranges["Upper Limit"])
# #     range_per = np.array(random * percent.iat[i,2])
# # =============================================================================
# 
# #car_mul = range_per.cr(oldcars.at[:10,1])
# =============================================================================
