# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:28:13 2019

@author: rhbar
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 

mastersheet = pd.read_csv("mastersheet.csv")
gas_saved = []

#print (type(len(rangesheet.index)))
#print (type(len(rangesheet.columns)))
def gas_calculation():
	for j in range(13):
		old_gas_year_0 = []
		new_gas_year_0 = []
		for i in range(len(mastersheet.index)):
			range_select = mastersheet.iat[i,j+7]
			old_car_mileage = mastersheet.iat[i,3]
			new_car_mileage = mastersheet.iat[i,6]
			if range_select == 1:
				miles_travelled = np.random.uniform(1, 1000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 2:
				miles_travelled = np.random.uniform(1000, 2000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 3:
				miles_travelled = np.random.uniform(2000, 4000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 4:
				miles_travelled = np.random.uniform(4000, 6000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 5:
				miles_travelled = np.random.uniform(6000, 8000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 6:
				miles_travelled = np.random.uniform(8000, 10000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 7:
				miles_travelled = np.random.uniform(10000, 12000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 8:
				miles_travelled = np.random.uniform(12000, 15000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 9:
				miles_travelled = np.random.uniform(15000, 20000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 10:
				miles_travelled = np.random.uniform(20000, 30000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			elif range_select == 11:
				miles_travelled = np.random.uniform(30000, 40000)
				old_gas_used = miles_travelled / old_car_mileage
				new_gas_used = miles_travelled / new_car_mileage
				old_gas_year_0.append(old_gas_used)
				new_gas_year_0.append(new_gas_used)
			else:
				pass
		difference = sum(old_gas_year_0) - sum(new_gas_year_0)
		gas_saved.append(difference)

def MonteCarloPlot(abcd):
	confidence_level = 0.05
	z_crit = stats.norm.ppf(1 - confidence_level/2)
	MonteCarloMean = np.array([np.average(abcd[0:i]) for i in range(len(abcd))])
	CI_Confidence = z_crit * np.array([stats.sem(abcd[0:i]) for i in range(len(abcd))])
	plt.figure()
	plt.plot(range(len(MonteCarloMean)), MonteCarloMean, 'b', label = "Mean")
	plt.plot(range(len(MonteCarloMean)), MonteCarloMean - CI_Confidence, 'g', label = "Lower Limit")
	plt.plot(range(len(MonteCarloMean)), MonteCarloMean + CI_Confidence, 'r', label = "Upper Limit")
	plt.xlabel("Trials")
	plt.ylabel("Average")
	plt.legend(loc = 'best')

	pass

for i in range(1):
	gas_calculation()
	print ("Iteration", i)
    
year0 = gas_saved[0::13]
Year_0 = sum(year0)

year1 = gas_saved[1::13]
Year_1 = Year_0 + sum(year1)

year2 = gas_saved[2::13]
Year_2 = Year_1 + sum(year2)

year3 = gas_saved[3::13]
Year_3 = Year_2 + sum(year3)

year4 = gas_saved[4::13]
Year_4 = Year_3 + sum(year4)

year5 = gas_saved[5::13]
Year_5 = Year_4 + sum(year5)

year6 = gas_saved[6::13]
Year_6 = Year_5 + sum(year6)

year7 = gas_saved[7::13]
Year_7 = Year_6 + sum(year7)

year8 = gas_saved[8::13]
Year_8 = Year_7 + sum(year8)

year9 = gas_saved[9::13]
Year_9 = Year_8 + sum(year9)

year10 = gas_saved[10::13]
Year_10 =Year_9 + sum(year10)

year11 = gas_saved[11::13]
Year_11 = Year_10 + sum(year11)

year12 = gas_saved[12::13]
Year_12 = Year_11 + sum(year12)

#confidence_level = 0.05
#z_crit = stats.norm.ppf(1 - confidence_level/2)
#
#mc_year0 = np.array([np.average(year0[0:i]) for i in range(len(year0))])
#year0_ci = z_crit * np.array([stats.sem(year0[0:i]) for i range(len(year0))])
print (Year_0)
print (Year_1)
print (Year_2)
print (Year_3)
print (Year_4)
print (Year_5)
print (Year_6)
print (Year_7)
print (Year_8)
print (Year_9)
print (Year_10)
print (Year_11)
print (Year_12)
print (year0)
print (year1)
print (year2)
print (year3)
print (year4)
print (year5)
print (year6)
print (year7)
print (year8)
print (year9)
print (year10)
print (year11)
print (year12)

MonteCarloPlot(year0)
MonteCarloPlot(year1)
MonteCarloPlot(year2)
MonteCarloPlot(year3)
MonteCarloPlot(year4)
MonteCarloPlot(year5)
MonteCarloPlot(year6)
MonteCarloPlot(year7)
MonteCarloPlot(year8)
MonteCarloPlot(year9)
MonteCarloPlot(year10)
MonteCarloPlot(year11)
MonteCarloPlot(year12)


import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)