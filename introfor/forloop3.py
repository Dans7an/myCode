#!/usr/bin/env python3
""" nesting an dictionaries inside of lists"""

def main():
    # list of dictionaries
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    # loop across the list called farms
    for farm in farms:
            print("\nThe farm name is " + farm["name"])
            for agric in farm["agriculture"]:
                print("Has got", agric)

main()
