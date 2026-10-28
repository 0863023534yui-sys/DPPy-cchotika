#!/usr/bin/env python3 
a = str(input("Give me a number: "))
num = float(a) 

if num % 1 == 0:
        print("This number is an integer.")
else:
        print("This number is a decimal.")