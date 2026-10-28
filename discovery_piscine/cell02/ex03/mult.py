#!/usr/bin/env python3
firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))
fullnum = firstnum * secondnum

if fullnum > 1:
    print(fullnum)
    print("This number is a positive number.")
elif fullnum == 0:
    print(fullnum)
    print("This number is equal to zero.")
elif fullnum < 1:
    print(fullnum)
    print("This number is a negative number.")