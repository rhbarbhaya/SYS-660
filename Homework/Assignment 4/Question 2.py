# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 02:06:31 2019

@author: Rushabh Barbhaya

Question 2
You are trying to quantitatively estimate the impact of Stevens’ commuters on roadway congestion in order to determine alternative bus routes to reduce the number of drivers. To do so, you will estimate the total number of miles traveled by people driving to campus on an average weekday, including all faculty, staff and students. Estimate the total number of miles driven, and report a range of values. You must source all the documents and/or websites you use to find data.
"""

import scipy.stats as stats
import numpy as np 
import matplotlib.pyplot as plt 

def freshmen(iter1):
	global undergrad_student
	undergrad_student = 0
	for i in range(iter1):
		gen1 = np.random.uniform(0.2, 0.8)
		undergrad_student += gen1
	undergrad.append(undergrad_student)
	return undergrad_student

def gradu(iter2):
	global grad_students
	grad_students = 0
	for i in range(iter2):
		gen2 = np.random.uniform(1,3)
		grad_students += gen2
	graduate.append(grad_students)
	return grad_students

def staff(iter3):
	global staf
	staf = 0
	for i in range(iter3):
		gen3 = np.random.uniform(2,7)
		staf += gen3
	stevens_faculty.append(staf)
	pass

def prof(iter4):
	global faculty
	faculty = 0
	for i in range(iter4):
		gen4 = np.random.uniform(0,1)
		faculty += gen4
		pass
	for i in range(iter4):
		gen5 = np.random.uniform(3,5)
		faculty += gen5
		pass
	for i in range(iter4):
		gen6 = np.random.uniform(6,10)
		faculty += gen6
		pass
	stevens_staff.append(faculty)
	pass

def dataset():
	sum_miles = undergrad_student + grad_students + staf + faculty
	fullset.append(sum_miles)
	pass

undergrad = []
graduate = []
stevens_faculty = []
stevens_staff = []
fullset = []

iter1 = 3431
iter2 = 3498
iter3 = 573
iter4 = int(291/3)

iteration = 100

for i in range(iteration):
    freshmen(iter1)
    gradu(iter2)
    staff(iter3)
    prof(iter4)
    dataset()
    pass

confidence_level = 0.05
z_crit = stats.norm.ppf(1 - confidence_level/2)

total_undergrad = np.array([np.average(undergrad[0:i]) for i in range(len(undergrad))])
undergrad_ci = z_crit * np.array([stats.sem(undergrad[0:i]) for i in range(len(undergrad))])

total_grad = np.array([np.average(graduate[0:i]) for i in range(len(graduate))])
grad_ci = z_crit * np.array([stats.sem(graduate[0:i]) for i in range(len(graduate))])

total_facu = np.array([np.average(stevens_faculty[0:i]) for i in range(len(stevens_faculty))])
facu_ci = z_crit * np.array([stats.sem(stevens_faculty[0:i]) for i in range(len(stevens_faculty))])

total_staff = np.array([np.average(stevens_staff[0:i]) for i in range(len(stevens_staff))])
staff_ci = z_crit * np.array([stats.sem(stevens_staff[0:i]) for i in range(len(stevens_staff))])

total_ds = np.array([np.average(fullset[0:i]) for i in range(len(fullset))])
ds_ci = z_crit * np.array([stats.sem(fullset[0:i]) for i in range(len(fullset))])

plt.figure()
plt.plot(range(len(undergrad)), undergrad, 'b', label = "Mean")
plt.plot(range(len(undergrad)), undergrad - undergrad_ci, 'g', label = "Lower Limit")
plt.plot(range(len(undergrad)), undergrad + undergrad_ci, 'r', label = "Upper Limit")
plt.xlabel("Trials")
plt.ylabel("Average miles by undergrad")
plt.legend(loc = 'best')

plt.figure()
plt.plot(range(len(graduate)), graduate, 'b', label = "Mean")
plt.plot(range(len(graduate)), graduate - grad_ci, 'g', label = "Lower Limit")
plt.plot(range(len(graduate)), graduate + grad_ci, 'r', label = "Upper Limit")
plt.xlabel("Trials")
plt.ylabel("Average miles by grad")
plt.legend(loc = 'best')

plt.figure()
plt.plot(range(len(total_facu)), total_facu, 'b', label = "Mean")
plt.plot(range(len(total_facu)), total_facu - facu_ci, 'g', label = "Lower Limit")
plt.plot(range(len(total_facu)), total_facu + facu_ci, 'r', label = "Upper Limit")
plt.xlabel("Trials")
plt.ylabel("Average miles by faculty")
plt.legend(loc = 'best')

plt.figure()
plt.plot(range(len(total_staff)), total_staff, 'b', label = "Mean")
plt.plot(range(len(total_staff)), total_staff - staff_ci, 'g', label = "Lower Limit")
plt.plot(range(len(total_staff)), total_staff + staff_ci, 'r', label = "Upper Limit")
plt.xlabel("Trials")
plt.ylabel("Average miles by staff")
plt.legend(loc = 'best')

plt.figure()
plt.plot(range(len(total_ds)), total_ds, 'b', label = "Mean")
plt.plot(range(len(total_ds)), total_ds - ds_ci, 'g', label = "Lower Limit")
plt.plot(range(len(total_ds)), total_ds + ds_ci, 'r', label = "Upper Limit")
plt.xlabel("Trials")
plt.ylabel("Average miles by everyone")
plt.legend(loc = 'best')

print ("\n\n--------------------------------")
print ("Average after 100 iterations of undergrad: {:.3f}".format(total_undergrad[-1]))
print ("Lower limit of 95%CI: {:.3f}".format(total_undergrad[-1] - undergrad_ci[-1]))
print ("Upper limit of 95%CI: {:.3f}".format(total_undergrad[-1] + undergrad_ci[-1]))
print ("--------------------------------")
print ("Average after 100 iterations of grad: {:.3f}".format(total_grad[-1]))
print ("Lower limit of 95%CI: {:.3f}".format(total_grad[-1] - grad_ci[-1]))
print ("Upper limit of 95%CI: {:.3f}".format(total_grad[-1] + grad_ci[-1]))
print ("--------------------------------")
print ("Average after 100 iterations of faculty: {:.3f}".format(total_facu[-1]))
print ("Lower limit of 95%CI: {:.3f}".format(total_facu[-1] - facu_ci[-1]))
print ("Upper limit of 95%CI: {:.3f}".format(total_facu[-1] + facu_ci[-1]))
print ("--------------------------------")
print ("Average after 100 iterations of staff: {:.3f}".format(total_staff[-1]))
print ("Lower limit of 95%CI: {:.3f}".format(total_staff[-1] - staff_ci[-1]))
print ("Upper limit of 95%CI: {:.3f}".format(total_staff[-1] + staff_ci[-1]))
print ("--------------------------------")
print ("Average after 100 iterations for everyone: {:.3f}".format(total_ds[-1]))
print ("Lower limit of 95%CI: {:.3f}".format(total_ds[-1] - ds_ci[-1]))
print ("Upper limit of 95%CI: {:.3f}".format(total_ds[-1] + ds_ci[-1]))