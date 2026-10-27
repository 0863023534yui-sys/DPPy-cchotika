#!/usr/bin/env python3
sum = int(input("Enter a number less than 25: "))
while sum < 25: 
    print(f"Inside the loop, my variable is {sum}")
    if (sum == 26):
        break
    sum += 1
