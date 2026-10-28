#!/usr/bin/env python3
i = str(input("Give me a number: "))
num = float(i)
if num % 1 == 0: #checks if it is a whole number.
    print(int(num))
else:
    print(int(num) + 1)