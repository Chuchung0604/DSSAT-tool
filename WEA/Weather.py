# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:13:16 2022

@author: ccchen
"""
import csv

def dayNumbers(year):
    if year%4 == 0:
        return 366
    else:
        return 365

def readValue(lon,lat,year,weatype):

    Value = []
    location = ["北部","中部","南部","東部"]

    isFind = False # refresh in each year loop
    for loc in location:
        if isFind == True:
            break
        filename = "WeaHist/TReAD_日資料_%s_%s/TReAD_日資料_%s_%s_%d.csv" %(loc,weatype,loc,weatype,year)
                
        with open(filename, newline='') as readfile:
            wea = csv.reader(readfile, delimiter = ',')
            next(wea) # skip header
            for row in wea:
                if float(row[0]) == lon:
                    if float(row[1]) == lat:
                        #isFind = True
                        for d in range(dayNumbers(year) + 2):
                            if d < 2:
                                continue
                            Value.append(float(row[d]))
    return Value # end of function readTemp

