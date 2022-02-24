# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:35:33 2019

@author: rhbar
"""
import csv
import pandas as pd
import numpy as np
from collections import Counter

range_sheet = pd.read_csv("range.csv")
range_sheet = range_sheet.set_index("Unnamed: 0")

year_select = range_sheet.index.tolist()
range_select = list(range_sheet.columns.values)

iter_keepers = []

Year0 = []
Year1 = []
Year2 = []
Year3 = []
Year4 = []
Year5 = []
Year6 = []
Year7 = []
Year8 = []
Year9 = []
Year10 = []
Year11 = []
Year12 = []

for i in year_select:
    for j in range_select:
        counters = i + " " + j
        iter_keepers.append(counters)
        
count = Counter(iter_keepers)

def RangeForYear0():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 0 Range 1"] <= (range_sheet.iat[0,0])) and round_gen == 1:
		count.update(["Year 0 Range 1"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 2"] <= (range_sheet.iat[0,1])) and round_gen == 2:
		count.update(["Year 0 Range 2"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 3"] <= (range_sheet.iat[0,2])) and round_gen == 3:
		count.update(["Year 0 Range 3"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 4"] <= (range_sheet.iat[0,3])) and round_gen == 4:
		count.update(["Year 0 Range 4"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 5"] <= (range_sheet.iat[0,4])) and round_gen == 5:
		count.update(["Year 0 Range 5"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 6"] <= (range_sheet.iat[0,5])) and round_gen == 6:
		count.update(["Year 0 Range 6"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 7"] <= (range_sheet.iat[0,6])) and round_gen == 7:
		count.update(["Year 0 Range 7"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 8"] <= (range_sheet.iat[0,7])) and round_gen == 8:
		count.update(["Year 0 Range 8"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 9"] <= (range_sheet.iat[0,8])) and round_gen == 9:
		count.update(["Year 0 Range 9"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 10"] <= (range_sheet.iat[0,9])) and round_gen == 10:
		count.update(["Year 0 Range 10"])
		Year0.append(round_gen)

	elif (count["Year 0 Range 11"] <= (range_sheet.iat[0,10])) and round_gen == 11:
		count.update(["Year 0 Range 11"])
		Year0.append(round_gen)

	else:
		pass

def RangeForYear1():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 1 Range 1"] <= (range_sheet.iat[1,0])) and round_gen == 1:
		count.update(["Year 1 Range 1"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 2"] <= (range_sheet.iat[1,1])) and round_gen == 2:
		count.update(["Year 1 Range 2"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 3"] <= (range_sheet.iat[1,2])) and round_gen == 3:
		count.update(["Year 1 Range 3"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 4"] <= (range_sheet.iat[1,3])) and round_gen == 4:
		count.update(["Year 1 Range 4"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 5"] <= (range_sheet.iat[1,4])) and round_gen == 5:
		count.update(["Year 1 Range 5"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 6"] <= (range_sheet.iat[1,5])) and round_gen == 6:
		count.update(["Year 1 Range 6"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 7"] <= (range_sheet.iat[1,6])) and round_gen == 7:
		count.update(["Year 1 Range 7"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 8"] <= (range_sheet.iat[1,7])) and round_gen == 8:
		count.update(["Year 1 Range 8"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 9"] <= (range_sheet.iat[1,8])) and round_gen == 9:
		count.update(["Year 1 Range 9"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 10"] <= (range_sheet.iat[1,9])) and round_gen == 10:
		count.update(["Year 1 Range 10"])
		Year1.append(round_gen)

	elif (count["Year 1 Range 11"] <= (range_sheet.iat[1,10])) and round_gen == 11:
		count.update(["Year 1 Range 11"])
		Year1.append(round_gen)

	else:
		pass

def RangeForYear2():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 2 Range 1"] <= (range_sheet.iat[2,0])) and round_gen == 1:
		count.update(["Year 2 Range 1"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 2"] <= (range_sheet.iat[2,1])) and round_gen == 2:
		count.update(["Year 2 Range 2"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 3"] <= (range_sheet.iat[2,2])) and round_gen == 3:
		count.update(["Year 2 Range 3"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 4"] <= (range_sheet.iat[2,3])) and round_gen == 4:
		count.update(["Year 2 Range 4"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 5"] <= (range_sheet.iat[2,4])) and round_gen == 5:
		count.update(["Year 2 Range 5"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 6"] <= (range_sheet.iat[2,5])) and round_gen == 6:
		count.update(["Year 2 Range 6"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 7"] <= (range_sheet.iat[2,6])) and round_gen == 7:
		count.update(["Year 2 Range 7"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 8"] <= (range_sheet.iat[2,7])) and round_gen == 8:
		count.update(["Year 2 Range 8"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 9"] <= (range_sheet.iat[2,8])) and round_gen == 9:
		count.update(["Year 2 Range 9"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 10"] <= (range_sheet.iat[2,9])) and round_gen == 10:
		count.update(["Year 2 Range 10"])
		Year2.append(round_gen)

	elif (count["Year 2 Range 11"] <= (range_sheet.iat[2,10])) and round_gen == 11:
		count.update(["Year 2 Range 11"])
		Year2.append(round_gen)

	else:
		pass

def RangeForYear3():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 3 Range 1"] <= (range_sheet.iat[3,0])) and round_gen == 1:
		count.update(["Year 3 Range 1"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 2"] <= (range_sheet.iat[3,1])) and round_gen == 2:
		count.update(["Year 3 Range 2"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 3"] <= (range_sheet.iat[3,2])) and round_gen == 3:
		count.update(["Year 3 Range 3"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 4"] <= (range_sheet.iat[3,3])) and round_gen == 4:
		count.update(["Year 3 Range 4"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 5"] <= (range_sheet.iat[3,4])) and round_gen == 5:
		count.update(["Year 3 Range 5"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 6"] <= (range_sheet.iat[3,5])) and round_gen == 6:
		count.update(["Year 3 Range 6"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 7"] <= (range_sheet.iat[3,6])) and round_gen == 7:
		count.update(["Year 3 Range 7"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 8"] <= (range_sheet.iat[3,7])) and round_gen == 8:
		count.update(["Year 3 Range 8"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 9"] <= (range_sheet.iat[3,8])) and round_gen == 9:
		count.update(["Year 3 Range 9"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 10"] <= (range_sheet.iat[3,9])) and round_gen == 10:
		count.update(["Year 3 Range 10"])
		Year3.append(round_gen)

	elif (count["Year 3 Range 11"] <= (range_sheet.iat[3,10])) and round_gen == 11:
		count.update(["Year 3 Range 11"])
		Year3.append(round_gen)

	else:
		pass

def RangeForYear4():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 4 Range 1"] <= (range_sheet.iat[4,0])) and round_gen == 1:
		count.update(["Year 4 Range 1"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 2"] <= (range_sheet.iat[4,1])) and round_gen == 2:
		count.update(["Year 4 Range 2"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 3"] <= (range_sheet.iat[4,2])) and round_gen == 3:
		count.update(["Year 4 Range 3"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 4"] <= (range_sheet.iat[4,3])) and round_gen == 4:
		count.update(["Year 4 Range 4"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 5"] <= (range_sheet.iat[4,4])) and round_gen == 5:
		count.update(["Year 4 Range 5"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 6"] <= (range_sheet.iat[4,5])) and round_gen == 6:
		count.update(["Year 4 Range 6"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 7"] <= (range_sheet.iat[4,6])) and round_gen == 7:
		count.update(["Year 4 Range 7"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 8"] <= (range_sheet.iat[4,7])) and round_gen == 8:
		count.update(["Year 4 Range 8"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 9"] <= (range_sheet.iat[4,8])) and round_gen == 9:
		count.update(["Year 4 Range 9"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 10"] <= (range_sheet.iat[4,9])) and round_gen == 10:
		count.update(["Year 4 Range 10"])
		Year4.append(round_gen)

	elif (count["Year 4 Range 11"] <= (range_sheet.iat[4,10])) and round_gen == 11:
		count.update(["Year 4 Range 11"])
		Year4.append(round_gen)

	else:
		pass

def RangeForYear5():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 5 Range 1"] <= (range_sheet.iat[5,0])) and round_gen == 1:
		count.update(["Year 5 Range 1"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 2"] <= (range_sheet.iat[5,1])) and round_gen == 2:
		count.update(["Year 5 Range 2"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 3"] <= (range_sheet.iat[5,2])) and round_gen == 3:
		count.update(["Year 5 Range 3"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 4"] <= (range_sheet.iat[5,3])) and round_gen == 4:
		count.update(["Year 5 Range 4"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 5"] <= (range_sheet.iat[5,4])) and round_gen == 5:
		count.update(["Year 5 Range 5"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 6"] <= (range_sheet.iat[5,5])) and round_gen == 6:
		count.update(["Year 5 Range 6"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 7"] <= (range_sheet.iat[5,6])) and round_gen == 7:
		count.update(["Year 5 Range 7"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 8"] <= (range_sheet.iat[5,7])) and round_gen == 8:
		count.update(["Year 5 Range 8"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 9"] <= (range_sheet.iat[5,8])) and round_gen == 9:
		count.update(["Year 5 Range 9"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 10"] <= (range_sheet.iat[5,9])) and round_gen == 10:
		count.update(["Year 5 Range 10"])
		Year5.append(round_gen)

	elif (count["Year 5 Range 11"] <= (range_sheet.iat[5,10])) and round_gen == 11:
		count.update(["Year 5 Range 11"])
		Year5.append(round_gen)

	else:
		pass

def RangeForYear6():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 6 Range 1"] <= (range_sheet.iat[6,0])) and round_gen == 1:
		count.update(["Year 6 Range 1"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 2"] <= (range_sheet.iat[6,1])) and round_gen == 2:
		count.update(["Year 6 Range 2"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 3"] <= (range_sheet.iat[6,2])) and round_gen == 3:
		count.update(["Year 6 Range 3"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 4"] <= (range_sheet.iat[6,3])) and round_gen == 4:
		count.update(["Year 6 Range 4"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 5"] <= (range_sheet.iat[6,4])) and round_gen == 5:
		count.update(["Year 6 Range 5"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 6"] <= (range_sheet.iat[6,5])) and round_gen == 6:
		count.update(["Year 6 Range 6"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 7"] <= (range_sheet.iat[6,6])) and round_gen == 7:
		count.update(["Year 6 Range 7"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 8"] <= (range_sheet.iat[6,7])) and round_gen == 8:
		count.update(["Year 6 Range 8"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 9"] <= (range_sheet.iat[6,8])) and round_gen == 9:
		count.update(["Year 6 Range 9"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 10"] <= (range_sheet.iat[6,9])) and round_gen == 10:
		count.update(["Year 6 Range 10"])
		Year6.append(round_gen)

	elif (count["Year 6 Range 11"] <= (range_sheet.iat[6,10])) and round_gen == 11:
		count.update(["Year 6 Range 11"])
		Year6.append(round_gen)

	else:
		pass

def RangeForYear7():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 7 Range 1"] <= (range_sheet.iat[7,0])) and round_gen == 1:
		count.update(["Year 7 Range 1"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 2"] <= (range_sheet.iat[7,1])) and round_gen == 2:
		count.update(["Year 7 Range 2"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 3"] <= (range_sheet.iat[7,2])) and round_gen == 3:
		count.update(["Year 7 Range 3"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 4"] <= (range_sheet.iat[7,3])) and round_gen == 4:
		count.update(["Year 7 Range 4"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 5"] <= (range_sheet.iat[7,4])) and round_gen == 5:
		count.update(["Year 7 Range 5"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 6"] <= (range_sheet.iat[7,5])) and round_gen == 6:
		count.update(["Year 7 Range 6"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 7"] <= (range_sheet.iat[7,6])) and round_gen == 7:
		count.update(["Year 7 Range 7"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 8"] <= (range_sheet.iat[7,7])) and round_gen == 8:
		count.update(["Year 7 Range 8"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 9"] <= (range_sheet.iat[7,8])) and round_gen == 9:
		count.update(["Year 7 Range 9"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 10"] <= (range_sheet.iat[7,9])) and round_gen == 10:
		count.update(["Year 7 Range 10"])
		Year7.append(round_gen)

	elif (count["Year 7 Range 11"] <= (range_sheet.iat[7,10])) and round_gen == 11:
		count.update(["Year 7 Range 11"])
		Year7.append(round_gen)

	else:
		pass

def RangeForYear8():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 8 Range 1"] <= (range_sheet.iat[8,0])) and round_gen == 1:
		count.update(["Year 8 Range 1"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 2"] <= (range_sheet.iat[8,1])) and round_gen == 2:
		count.update(["Year 8 Range 2"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 3"] <= (range_sheet.iat[8,2])) and round_gen == 3:
		count.update(["Year 8 Range 3"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 4"] <= (range_sheet.iat[8,3])) and round_gen == 4:
		count.update(["Year 8 Range 4"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 5"] <= (range_sheet.iat[8,4])) and round_gen == 5:
		count.update(["Year 8 Range 5"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 6"] <= (range_sheet.iat[8,5])) and round_gen == 6:
		count.update(["Year 8 Range 6"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 7"] <= (range_sheet.iat[8,6])) and round_gen == 7:
		count.update(["Year 8 Range 7"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 8"] <= (range_sheet.iat[8,7])) and round_gen == 8:
		count.update(["Year 8 Range 8"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 9"] <= (range_sheet.iat[8,8])) and round_gen == 9:
		count.update(["Year 8 Range 9"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 10"] <= (range_sheet.iat[8,9])) and round_gen == 10:
		count.update(["Year 8 Range 10"])
		Year8.append(round_gen)

	elif (count["Year 8 Range 11"] <= (range_sheet.iat[8,10])) and round_gen == 11:
		count.update(["Year 8 Range 11"])
		Year8.append(round_gen)

	else:
		pass

def RangeForYear9():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 9 Range 1"] <= (range_sheet.iat[9,0])) and round_gen == 1:
		count.update(["Year 9 Range 1"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 2"] <= (range_sheet.iat[9,1])) and round_gen == 2:
		count.update(["Year 9 Range 2"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 3"] <= (range_sheet.iat[9,2])) and round_gen == 3:
		count.update(["Year 9 Range 3"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 4"] <= (range_sheet.iat[9,3])) and round_gen == 4:
		count.update(["Year 9 Range 4"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 5"] <= (range_sheet.iat[9,4])) and round_gen == 5:
		count.update(["Year 9 Range 5"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 6"] <= (range_sheet.iat[9,5])) and round_gen == 6:
		count.update(["Year 9 Range 6"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 7"] <= (range_sheet.iat[9,6])) and round_gen == 7:
		count.update(["Year 9 Range 7"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 8"] <= (range_sheet.iat[9,7])) and round_gen == 8:
		count.update(["Year 9 Range 8"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 9"] <= (range_sheet.iat[9,8])) and round_gen == 9:
		count.update(["Year 9 Range 9"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 10"] <= (range_sheet.iat[9,9])) and round_gen == 10:
		count.update(["Year 9 Range 10"])
		Year9.append(round_gen)

	elif (count["Year 9 Range 11"] <= (range_sheet.iat[9,10])) and round_gen == 11:
		count.update(["Year 9 Range 11"])
		Year9.append(round_gen)

	else:
		pass

def RangeForYear10():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 10 Range 1"] <= (range_sheet.iat[10,0])) and round_gen == 1:
		count.update(["Year 10 Range 1"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 2"] <= (range_sheet.iat[10,1])) and round_gen == 2:
		count.update(["Year 10 Range 2"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 3"] <= (range_sheet.iat[10,2])) and round_gen == 3:
		count.update(["Year 10 Range 3"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 4"] <= (range_sheet.iat[10,3])) and round_gen == 4:
		count.update(["Year 10 Range 4"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 5"] <= (range_sheet.iat[10,4])) and round_gen == 5:
		count.update(["Year 10 Range 5"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 6"] <= (range_sheet.iat[10,5])) and round_gen == 6:
		count.update(["Year 10 Range 6"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 7"] <= (range_sheet.iat[10,6])) and round_gen == 7:
		count.update(["Year 10 Range 7"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 8"] <= (range_sheet.iat[10,7])) and round_gen == 8:
		count.update(["Year 10 Range 8"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 9"] <= (range_sheet.iat[10,8])) and round_gen == 9:
		count.update(["Year 10 Range 9"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 10"] <= (range_sheet.iat[10,9])) and round_gen == 10:
		count.update(["Year 10 Range 10"])
		Year10.append(round_gen)

	elif (count["Year 10 Range 11"] <= (range_sheet.iat[10,10])) and round_gen == 11:
		count.update(["Year 10 Range 11"])
		Year10.append(round_gen)

	else:
		pass

def RangeForYear11():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 11 Range 1"] <= (range_sheet.iat[11,0])) and round_gen == 1:
		count.update(["Year 11 Range 1"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 2"] <= (range_sheet.iat[11,1])) and round_gen == 2:
		count.update(["Year 11 Range 2"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 3"] <= (range_sheet.iat[11,2])) and round_gen == 3:
		count.update(["Year 11 Range 3"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 4"] <= (range_sheet.iat[11,3])) and round_gen == 4:
		count.update(["Year 11 Range 4"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 5"] <= (range_sheet.iat[11,4])) and round_gen == 5:
		count.update(["Year 11 Range 5"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 6"] <= (range_sheet.iat[11,5])) and round_gen == 6:
		count.update(["Year 11 Range 6"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 7"] <= (range_sheet.iat[11,6])) and round_gen == 7:
		count.update(["Year 11 Range 7"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 8"] <= (range_sheet.iat[11,7])) and round_gen == 8:
		count.update(["Year 11 Range 8"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 9"] <= (range_sheet.iat[11,8])) and round_gen == 9:
		count.update(["Year 11 Range 9"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 10"] <= (range_sheet.iat[11,9])) and round_gen == 10:
		count.update(["Year 11 Range 10"])
		Year11.append(round_gen)

	elif (count["Year 11 Range 11"] <= (range_sheet.iat[11,10])) and round_gen == 11:
		count.update(["Year 11 Range 11"])
		Year11.append(round_gen)

	else:
		pass

def RangeForYear12():
	generator = np.random.uniform(1,11)
	round_gen = round(generator)

	if (count["Year 12 Range 1"] <= (range_sheet.iat[12,0])) and round_gen == 1:
		count.update(["Year 12 Range 1"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 2"] <= (range_sheet.iat[12,1])) and round_gen == 2:
		count.update(["Year 12 Range 2"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 3"] <= (range_sheet.iat[12,2])) and round_gen == 3:
		count.update(["Year 12 Range 3"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 4"] <= (range_sheet.iat[12,3])) and round_gen == 4:
		count.update(["Year 12 Range 4"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 5"] <= (range_sheet.iat[12,4])) and round_gen == 5:
		count.update(["Year 12 Range 5"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 6"] <= (range_sheet.iat[12,5])) and round_gen == 6:
		count.update(["Year 12 Range 6"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 7"] <= (range_sheet.iat[12,6])) and round_gen == 7:
		count.update(["Year 12 Range 7"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 8"] <= (range_sheet.iat[12,7])) and round_gen == 8:
		count.update(["Year 12 Range 8"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 9"] <= (range_sheet.iat[12,8])) and round_gen == 9:
		count.update(["Year 12 Range 9"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 10"] <= (range_sheet.iat[12,9])) and round_gen == 10:
		count.update(["Year 12 Range 10"])
		Year12.append(round_gen)

	elif (count["Year 12 Range 11"] <= (range_sheet.iat[12,10])) and round_gen == 11:
		count.update(["Year 12 Range 11"])
		Year12.append(round_gen)

	else:
		pass

while len(Year0) <= 690113:
	RangeForYear0()
print ("Year 0 - Done!")

while len(Year1) <= 690113:
	RangeForYear1()
print ("Year 1 - Done!")

while len(Year2) <= 690113:
	RangeForYear2()
print ("Year 2 - Done!")

while len(Year3) <= 690113:
	RangeForYear3()
print ("Year 3 - Done!")

while len(Year4) <= 690113:
	RangeForYear4()
print ("Year 4 - Done!")

while len(Year5) <= 690113:
	RangeForYear5()
print ("Year 5 - Done!")

while len(Year6) <= 690113:
	RangeForYear6()
print ("Year 6 - Done!")

while len(Year7) <= 690113:
	RangeForYear7()
print ("Year 7 - Done!")

while len(Year8) <= 690113:
	RangeForYear8()
print ("Year 8 - Done!")

while len(Year9) <= 690113:
	RangeForYear9()
print ("Year 9 - Done!")

while len(Year10) <= 690113:
	RangeForYear10()
print ("Year 10 - Done!")

while len(Year11) <= 690113:
	RangeForYear11()
print ("Year 11 - Done!")

while len(Year12) <= 690113:
	RangeForYear12()
print ("Year 12 - Done!")

rows = zip(Year0, Year1, Year2, Year3, Year4, Year5, Year6, Year7, Year8, Year9, Year10, Year11, Year12)
with open("cars_dev3.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    for i in rows:
        writer.writerow(i)