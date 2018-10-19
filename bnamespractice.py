#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:32:53 2017

@author: alinasabirianova
"""


import pandas as pd

df = pd.read_csv("baby-names.csv")

#step 1
mostpop = df["percent"].idxmax()
print("Name " + str(df.loc[mostpop]["name"]) + " was given to " + str(df.percent.max()*100) + " of babies in " + str(df.loc[mostpop].year))

#step2



"""
gender = input("Gender: ")
style = input("Style: ")

if gender == "boy":
    sf = df[df["sex"] == "boy"]
    if style == "modern":
        sf = sf[sf["year"] >= 1990]
        mostpop = sf["percent"].idxmax()
        print("We suggest the name " + str(sf.loc[mostpop]["name"]))
    if style == "classic":
        sf = sf[sf["year"] < 1990]
        mostpop = sf["percent"].idxmax()
        print("We suggest the name " + str(sf.loc[mostpop]["name"]))
    if style == "none":
        mostpop = sf["percent"].idxmax()
        print("We suggest the name " + str(sf.loc[mostpop]["name"]))
if gender == "girl":
    sf = df[df["sex"] == "girl"]
    if style == "modern":
        sf = sf[sf["year"] >= 1990]
        mostpop = sf["percent"].idxmax()
        print("We suggest the name " + str(sf.loc[mostpop]["name"]))
    if style == "classic":
        sf = sf[sf["year"] < 1990]
        mostpop = sf["percent"].idxmax()
        print("We suggest the name " + str(sf.loc[mostpop]["name"]))
    if style == "none":
        mostpop = sf["percent"].idxmax()
        print("We suggest the name " + str(sf.loc[mostpop]["name"]))  
"""        
#step3

name = input("Name: ")
gender = input("Gender: ")

gf = df[(df["name"] == name) & (df["sex"] == gender)]
mostpop = gf["percent"].idxmax()
print(str(gf.loc[mostpop]["name"]) + " was the most popular name in the year " + str(gf.loc[mostpop]["year"]))       

     
        
  