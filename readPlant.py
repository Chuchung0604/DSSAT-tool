# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:43:49 2022

@author: user
"""
import csv

outputName = "PlantGro.OUT"
prefix = "TARI"

isFoundRun = False
isFoundHeader = False
f = open(outputName, 'r')
counter = 0
header = []
for line in f.readlines():
    counter += 1
    row = line.split()
    if len(row) == 0:
        continue
    
    if row[0] == "*RUN":
        isFoundRun = True
        print(counter,row[1],row[3])
        # open csv file
        f = open("%s%s.csv"%(prefix, row[3]),'w',newline='')
        writer = csv.writer(f)
    
    if isFoundHeader == False and row[0] == "@YEAR":
        #writer.writerow(row)
        for r in row:
            if "@YEAR" in r:
                r_new = r.replace("@YEAR","YEAR")
                header.append(r_new)
            elif "#" in r:
                r_new = r.replace("#","_")
                header.append(r_new)
            elif "%" in r:
                r_new = r.replace("%","_")
                header.append(r_new)
            else:
                header.append(r)
        writer.writerow(header)        
        #print(row[0],row[1],row[2],row[3])
        

        length = len(row)
        isFoundHeader = True
        header = []
        continue
        
    if isFoundHeader == True and len(row) == length:
        #print(row[0],row[1],row[2])
        writer.writerow(row)
    elif isFoundHeader == True and isFoundRun == True:
        isFoundHeader = False
        ifFoundRun = False
        f.close()
        
    
f.close()    

