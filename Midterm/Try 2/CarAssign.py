# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:13:11 2019

@author: rhbar
"""

import numpy as np
import pandas as pd
from collections import Counter
import csv

RangeSheet = pd.read_csv("RangeSheet.csv")
#print (RangeSheet.head())
NumberOfCars = pd.read_csv("NoCars.csv")
NumberOfCars = NumberOfCars.set_index("Number of Car")
#print (NumberOfCars.head())
CarsAssigned = []
counter = Counter()

def Assign_Cars():
	Rand = np.random.uniform(1,10)
	Round_Rand = round(Rand)
	return Round_Rand

def CarNumber(number):
	rowid = number - 1
	if counter[number] <= (NumberOfCars.iat[rowid,2]):
		counter.update([number])
		CarsAssigned.append(number)
	else:
		pass
	pass

while len(CarsAssigned) <= NumberOfCars["Rounded of"].sum():
	number = Assign_Cars()
	CarNumber(number)

with open("Round2.csv", "w") as f:
	writer = csv.writer(f, lineterminator = "\n")
	for i in CarsAssigned:
		writer.writerow([i])

print ("DOne!")


import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)