# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:28:41 2019

@author: rhbar
"""
import pandas as pd
jup = pd.read_csv("cy17-all-enplanements.csv")
jup["State"] = "AB"