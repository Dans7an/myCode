#!/usr/bin/env python3

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()

## Iterate through configlist
for x in configlist:
    print(x.strip())

## Always close your file
configfile.close()
