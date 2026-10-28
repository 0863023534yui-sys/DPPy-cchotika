#!/usr/bin/env python3
original = [2, 8, 9, 48, 8, 22, -12, 2]
new = [] 

for i in original:
    if i > 5:
        v = i + 2
        if v not in new:
            new.append(v)
print(original)
print(new)