#!/usr/bin/env python3
""" if, elif, else - A simple program using conditionals to make a decision."""

def main():
    message = 'The grade is'

    # wrap connection in a float() to accept decimals as numbers
    numberEntered = float(input("What is the percentage you want to grade?"))

    # if input value was higher or equal to 25
    if numberEntered <= 59:
        message = message + ' an F.'
    elif numberEntered <= 69:
        message = message + ' a D.'
    elif numberEntered <= 79:
        message = ' a C.'
    elif numberEntered <= 89:
        message = ' a B.'
    elif numberEntered <= 100:
        message = ' an A.'
    else:
        message ='You entered an invalid score. Try entering a score between 1 - 100%'
    print(message)

main()
