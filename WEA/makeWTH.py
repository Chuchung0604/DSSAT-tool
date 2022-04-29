# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:31:39 2022

@author: ccchen
"""
import Weather
ID = "TWTA"
LAT = 24.00
LON = 120.50
YEAR = 2020
ELEV = 80

Tmax_lst = Weather.readValue(LON, LAT, YEAR, "最高溫")
Tmin_lst = Weather.readValue(LON, LAT, YEAR, "最低溫")
WAT_lst = Weather.readValue(LON, LAT, YEAR, "日射量")
Precp_lst = Weather.readValue(LON, LAT, YEAR, "降雨量")

if YEAR < 2000:
    yrstr = YEAR - 1900

else:
    yrstr = YEAR - 2000

path = '%s%02d%s.WTH' %(ID,yrstr,'01')
#path = 'TWTA9201.WTH'

with open(path, 'w') as f:
    f.write("*WEATHER DATA : TAICHUNG,TAIWAN\n")
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
        solRad = WAT_lst[i]*60*60*24/1000000
        tmax = Tmax_lst[i]
        tmin = Tmin_lst[i]
        rain = Precp_lst[i]
        if rain < 100:
            f.write("%s \t %4.1f \t %4.1f \t %4.1f \t%5.1f\n" %(dateStr,solRad, tmax, tmin, rain))
        else:
            f.write("%s \t %4.1f \t %4.1f \t %4.1f \t%5.0f\n" %(dateStr,solRad, tmax, tmin, rain))
        print(i)