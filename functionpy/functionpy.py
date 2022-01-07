#!/usr/bin/env python3

# Function Grab Bag!
# Below are a collection of prompts to create functions! You must choose FOUR (4) to complete!

# Write a Python function to find the Max of three numbers.
def maxof3numbers(*nums):
    return max(nums)

# Write a Python function to sum all the numbers in a list.
def sumnumbers(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

# Write a Python function to multiply all the numbers in a list.
def multiplynumbers(nums):
    product = 1
    for i in nums:
        product *= i
    return product

def evennumbers(nums):
    arr = []
    for i in nums:
        if i % 2 == 0 :
            arr.append(i)
    return arr

def main():
    print("The max of 3 given numbers is",maxof3numbers(1,5,3))
    print("The sum of numbers in a list is",sumnumbers([8, 2, 3, 0, 7]))
    print("The product of numbers in a list is",multiplynumbers([8, 2, 3, -1, 7]))
    print("The even numbers in a list are",evennumbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
main()
