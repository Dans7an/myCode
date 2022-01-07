#!/usr/bin/env python3

with open("minichallenge01.txt","w") as filename:
    print("Year: 2022", file=filename)
    print("Month: Jan", file=filename)
    print("Day: 7", file=filename)

print("done writing")

with open("minichallenge01.txt","r") as filename: 
    filelist = filename.readlines()
    print(filelist)

print("Done reading")
