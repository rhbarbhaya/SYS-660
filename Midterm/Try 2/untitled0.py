# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:19:51 2019

@author: rhbar
"""

import csv
import numpy as np

counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0
counter_8 = 0
counter_9 = 0
counter_10 = 0

car_make = []

def gen():
	global counter_1
	global counter_2
	global counter_3
	global counter_4
	global counter_5
	global counter_6
	global counter_7
	global counter_8
	global counter_9
	global counter_10
	generator = np.random.uniform(1,10)
	round_generator = round(generator)
	
	if counter_1 <= 193231 and round_generator == 1:
	    counter_1 += 1
	    car_make.append(1)
	    return counter_1

	elif counter_2 <= 138022 and round_generator == 2:
	    counter_2 += 1
	    car_make.append(2)

	elif counter_3 <= 96615 and round_generator == 3:
	    counter_3 += 1
	    car_make.append(3)

	elif counter_4 <= 69010 and round_generator == 4:
	    counter_4 += 1
	    car_make.append(4)

	elif counter_5 <= 55208 and round_generator == 5:
	    counter_5 += 1
	    car_make.append(5)

	elif counter_6 <= 41406 and round_generator == 6:
	    counter_6 += 1
	    car_make.append(6)

	elif counter_7 <= 27604 and round_generator == 7:
	    counter_7 += 1
	    car_make.append(7)

	elif counter_8 <= 27604 and round_generator == 8:
	    counter_8 += 1
	    car_make.append(8)

	elif counter_9 <= 20702 and round_generator == 9:
	    counter_9 += 1
	    car_make.append(9)

	elif counter_10 <= 20702 and round_generator == 10:
	    counter_10 += 1
	    car_make.append(10)
	
while len(car_make) <= 690113:
    gen()

with open("cars_dev4.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    for i in car_make:
        writer.writerow([i])

print ("DOne!")	