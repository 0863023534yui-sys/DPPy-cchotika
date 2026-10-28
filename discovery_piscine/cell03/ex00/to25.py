#!/usr/bin/env python3
sum = int(input("Enter a number less than 25: "))
if sum > 25:
    print("ERROR")
else:
    while sum < 26: 
        print(f"Inside the loop, my variable is {sum}")
        if (sum == 25):
            break
        sum += 1