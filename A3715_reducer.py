#!/usr/bin/python

import sys
import operator

outputFile = open('reducer.txt', 'w')
previous_key = None
total = 0
inputFile = open('mapper.txt','r')
kvDict = {}

for line in inputFile:
    s = line.split("\t")
    s[1] = int(s[1].split("\n")[0])
    #print (s)
    key = s[0]
    value = s[1]
    if key in kvDict:
        value = kvDict[key]
        kvDict[key] = (int(value)+1)
        total = total + 1;
    else:
        kvDict[key] = value
        total = total + 1;
   
kvSorted = sorted(kvDict.items(), key=operator.itemgetter(1))

for group in kvSorted:
    print (group)
    outputFile.write(str(group[0]) + " --> " + str(group[1]) + "\n")

inputFile.close()
outputFile.close()
