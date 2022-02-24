# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:11:42 2019

@author: Rushabh Barbhaya
Subject : SYS 660

Question 1:
How many pounds of toothpaste are used in the US each day? You would need to
transfer all of this toothpaste to a certain location via 747 aircrafts. How many 747 aircrafts
would it take to move it.
Your assumptions and calculations should be very clear to comprehend. If you are using any data
from external sources do NOT forget to mention your source. What is your lower bound, upper
bound and best guess for your estimates.
"""

#Importing libraries for simulation
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

montecarlo = 11

def paste():
    paste_gen = np.random.triangular(0.02, 0.0283, 0.03)
    paste_gen = paste_gen / 16.0
    return paste_gen

def use():
    use_gen = np.random.triangular(0, 1, 2)
    if use_gen <= 0.5:
        use_gen = 0
    elif use_gen >= 1.5:
        use_gen = 2
    else:
        use_gen = 1
    return use_gen

def stat():
    global total_paste
    global _747used
    paste_used = []
    use_times = []
    for i in range(32839):
        toothpaste = paste()
        numberuse = use()
        toothpaste *= numberuse
        paste_used.append(toothpaste)
        use_times.append(numberuse)
    ds = pd.DataFrame(data = [use_times, paste_used]).transpose()
    ds = ds.rename(columns = {0: "Times Used", 1: "Paste Quantity"})
    total_paste = ds["Paste Quantity"].sum()*10000
    _747used = total_paste / 308000
    return total_paste, _747used

def averageset():
    avgToothpaste = 0
    avgAirplanes = 0
    for i in range(1, 11):
        stat()
        avgToothpaste += total_paste
        avgAirplanes += _747used
    avg_toothpaste.append(avgToothpaste/(i))
    avg_airplanes.append(avgAirplanes/(i))
   
avg_toothpaste = []
avg_airplanes = []

confidence_level = 0.05
z_crit = stats.norm.ppf(1 - confidence_level/2)

total_dataset = [averageset() for i in range(montecarlo)]
avgtoothpaste = np.array([np.average(avg_toothpaste[0:i]) for i in range(len(avg_toothpaste))])
paste_ci = z_crit * np.array([stats.sem(avg_toothpaste[0:i]) for i in range(len(avg_toothpaste))])

avgairplane = np.array([np.average(avg_airplanes[0:i]) for i in range(len(avg_airplanes))])
plane_ci = z_crit * np.array([stats.sem(avg_airplanes[0:i]) for i in range(len(avg_airplanes))])

plt.figure()
plt.plot(range(len(avgtoothpaste)), avgtoothpaste, 'b', label = "Mean")
plt.plot(range(len(avgtoothpaste)), avgtoothpaste - paste_ci, 'g', label = "Lower Limit")
plt.plot(range(len(avgtoothpaste)), avgtoothpaste + paste_ci, 'r', label = "Upper Limit")
plt.xlabel("iteration")
plt.ylabel("Mean toothpaste used (in pounds)")
plt.legend(loc = 'best')

plt.figure()
plt.plot(range(len(avgairplane)), avgairplane, 'b', label = "Mean")
plt.plot(range(len(avgairplane)), avgairplane - plane_ci, 'g', label = "Lower Limit")
plt.plot(range(len(avgairplane)), avgairplane + plane_ci, 'r', label = "Upper Limit")
plt.xlabel("iteration")
plt.ylabel("Mean airplanes in use")
plt.legend(loc = 'best')

print "Average after 10 iterations of event: {:.3f}".format(avgtoothpaste[-1])
print "Lower limit of 95%CI: {:.3f}".format(avgtoothpaste[-1] - paste_ci[-1])
print "Upper limit of 95%CI: {:.3f}".format(avgtoothpaste[-1] + paste_ci[-1])
print "--------------------------------------"
print "Average after 10 iterations of event: {:.3f}".format(avgairplane[-1])
print "Lower limit of 95%CI: {:.3f}".format(avgairplane[-1] - plane_ci[-1])
print "Upper limit of 95%CI: {:.3f}".format(avgairplane[-1] + plane_ci[-1])