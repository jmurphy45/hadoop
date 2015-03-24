#!/usr/bin/python

import sys

output = file('reducer.txt', 'w')
previous_key = None
total = 0
file = open('mapper.txt','r')
kvList = {}

for line in file:
    key, value = line.split("\t",1)
    if key in kvList:
        value = kvList[key]
        kvList[key] = (int(value)+1)
        total = total + 1;
    else:
        kvList[key] = value
        total = total + 1;
   
for key in kvList:
    print "Key = " + str(key) +  "\n" + "value = " + str(kvList[key])
    output.write(str(key) + " -> " + str(kvList[key]) + "\n")