# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:42:20 2019

@author: rhbar
"""
import pandas as pd

filename = pd.read_csv("cy17-cargo-airports.csv")

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
          "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
          "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
          "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
          "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
          "West Virginia", "Wisconsin", "Wyoming", "Northern Marina Islands", "American Samoa", "Guam",
          "Puerto Rico", "Virgin Islands"]

codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
         "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
         "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "MP",
         "AS", "GU", "PR", "VI"]

filename["State"] = filename.replace(codes, states)

regions = ["Alaskan", "Northwest Mountain", "Western Pacific", "Central", "Southwest", "Great Lakes",
           "New England", "Eastern", "Southern"]
region_codes = ["AL", "NM", "WP", "CE", "SW", "GL", "NE", "EA", "SO"]

filename["RO"] = filename["RO"].replace(region_codes, regions)
#filename = filename.drop([30, 62, 133, 389, 515, 516])
filename.rename(columns = {'RO': 'Region Operation'}, inplace = True)



#filename.to_csv("CY17 Cargo Airports.csv", index = None)