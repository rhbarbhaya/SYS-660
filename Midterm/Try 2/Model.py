# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:28:13 2019

@author: rhbar
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 
import csv
import time

start = time.time()
mastersheet = pd.read_csv("MasterList.csv")
rangevalue = pd.read_csv("Values.csv")
oldcargasuse = []
newcargasused = []

def oldcar(lowerlimit, upperlimit, old_mileage):
	gen = np.random.uniform(lowerlimit,upperlimit)
	oldgas = gen / old_mileage
	return oldgas

def newcar(lowerlimit, upperlimit, new_mileage):
	gen = np.random.uniform(lowerlimit, upperlimit)
	newgas = gen / new_mileage
	return newgas

def ranges(rowno, colno):
	range_select = (mastersheet.iat[rowno,colno])-1
	rowselect = rangevalue.iloc[[range_select]]
	lowerlimit = rowselect.iat[0,1]
	upperlimit = rowselect.iat[0,2]
	return lowerlimit, upperlimit

def milage(rowno):
	old_mileage = mastersheet.iat[rowno,3]
	new_mileage = mastersheet.iat[rowno,6]
	return old_mileage, new_mileage

def run(j):
    for i in range(len(mastersheet.index)):
        old_mileage, new_mileage = milage(i)
        lowerlimit,upperlimit = ranges(i, j)
        oldgas = oldcar(lowerlimit, upperlimit, old_mileage)
        newgas = newcar(lowerlimit, upperlimit, new_mileage)
        oldcargasuse.append(oldgas)
        newcargasused.append(newgas)

#for i in range(13):
    run(i+7)

import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
end = time.time()
print (end - start)