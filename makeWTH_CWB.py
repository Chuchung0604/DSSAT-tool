# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:09:06 2022

@author: user
"""
import csv

ID = "TWTB"
LAT = 24.00
LON = 120.50
YEAR = 2020
ELEV = 80

# Tmax_lst = Weather.readValue(LON, LAT, YEAR, "最高溫")
# Tmin_lst = Weather.readValue(LON, LAT, YEAR, "最低溫")
# WAT_lst = Weather.readValue(LON, LAT, YEAR, "日射量")
# Precp_lst = Weather.readValue(LON, LAT, YEAR, "降雨量")
Tmax_lst = []
Tmin_lst = []
SolRad_lst = []
Precp_lst = []
weaName = "CWB/G2F820_%d.csv" %YEAR

with open(weaName, newline='') as readfile:
    wea = csv.reader(readfile, delimiter = ',')
    next(wea)
    next(wea)
    for row in wea:
        if len(row[2])>0:
            Tmax_lst.append(float(row[2]))
        else: #missing value
            Tmax_lst.append(-99.0)
        if len(row[3])>0:    
            Tmin_lst.append(float(row[3]))
        else:
            Tmin_lst.append(-99.0)
        if len(row[6]) >0:    
            Precp_lst.append(float(row[6]))
        else:
            Precp_lst.append(-99.0)
        if len(row[7])>0 and float(row[7])> 0.5:
            SolRad_lst.append(float(row[7]))
        else:
            SolRad_lst.append(-99)
    # end of reading weafile


if YEAR < 2000:
    yrstr = YEAR - 1900

else:
    yrstr = YEAR - 2000

path = '%s%02d%s.WTH' %(ID,yrstr,'01')
#path = 'TWTA9201.WTH'

with open(path, 'w') as f:
    f.write("*WEATHER DATA : TAICHUNG_CWB,TAIWAN\n")
    f.write(" \n")
    f.write("@ INSI     LAT     LONG  ELEV   TAV   AMP  REFHT WNDHT\n")
    toWrite = "  %s\t %.2f \t %.2f   %3d   0.0   0.0  -99.0 -99.0\n" %(ID,LAT,LON,ELEV)
    f.write(toWrite)
    #f.write("\n")
    f.write("@DATE \t SRAD \t TMAX \t TMIN \t RAIN  \n")
    for i in range(len(Tmax_lst)):
        if YEAR < 2000:    
            dateStr = "%d%.3d" %(YEAR-1900, i+1)
        else:
            dateStr = "%d%.3d" %(YEAR-2000, i+1) 
        solRad = SolRad_lst[i]
        #solRad = WAT_lst[i]*60*60*24/1000000
        tmax = Tmax_lst[i]
        tmin = Tmin_lst[i]
        rain = Precp_lst[i]
        if rain < 100 and rain > -5:
            f.write("%s \t %4.1f \t %4.1f \t %4.1f \t%5.1f\n" %(dateStr,solRad, tmax, tmin, rain))
        else:
            f.write("%s \t %4.1f \t %4.1f \t %4.1f \t%5.0f\n" %(dateStr,solRad, tmax, tmin, rain))
        print(i+1)