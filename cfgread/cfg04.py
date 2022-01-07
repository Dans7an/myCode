#!/usr/bin/env python3

cfg_file = input("What file do you want to read?\n")
## create file object in "r"ead mode
with open(cfg_file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

# display numbers of lines in the vlanconfig.cfg
print(configlist.__len__())
print(configlist)
