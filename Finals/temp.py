# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import pandas as pd

bible = pd.read_csv("CY17 All Enplanements.csv")

_16sum = bible["CY 16 Enplanements"].sum()
_17sum = bible["CY 17 Enplanements"].sum()

_0bags16 = int(_16sum*(random.randint(22,26)/100))
_1bags16 = int(_16sum*(random.randint(57,61)/100))
_2bags16 = int(_16sum*(random.randint(13,17)/100))
_3bags16 = int(_16sum*(random.randint(0,1)/100))
_4bags16 = int(_16sum*(random.randint(0,1)/100))

_0bags17 = int(_17sum*(random.randint(22,26)/100))
_1bags17 = int(_17sum*(random.randint(57,61)/100))
_2bags17 = int(_17sum*(random.randint(13,17)/100))
_3bags17 = int(_17sum*(random.randint(0,1)/100))
_4bags17 = int(_17sum*(random.randint(0,1)/100))

Bags16 = 0*_0bags16 + _1bags16 + 2*_2bags16 + 3*_3bags16 + 4*_4bags16
print ("Bags16", Bags16/1000000, "Millions")



_1price = 30
_2price = 70
_3price = 100
_4price = 200

Price16 = _1price * _1bags16 + _2price * _2bags16 + _3price * _3bags16 + _4price * _4bags16
print ("Money in bags16", Price16/1000000000, "Billions")

Bags_Lost16 = Bags16 * 0.00315
print ("Lost bags16", Bags_Lost16/1000000, "Millions")

Liability16 = 0
for i in range(int(Bags_Lost16)):
    paisa = random.randint(0,3300)
    Liability16 += paisa
    pass
print ("Paid amount16", Liability16/1000000000, "Billions")

print ("\n\n\n\n")
Bags17 = 0*_0bags17 + _1bags17 + 2*_2bags17 + 3*_3bags17 + 4*_4bags17
print ("Bags17", Bags17/1000000, "Millions")

Price17 = _1price * _1bags17 + _2price * _2bags17 + _3price * _3bags17 + _4price * _4bags17
print ("Money in bags17", Price17/1000000000, "Billions")

Bags_Lost17 = Bags17 * 0.00245
print ("Lost bags17", Bags_Lost17/1000000, "Millions")

Liability17 = 0
for i in range(int(Bags_Lost17)):
    paisa = random.randint(0,3300)
    Liability17 += paisa
    pass
print ("Paid amount17", Liability17/1000000000, "Billions")