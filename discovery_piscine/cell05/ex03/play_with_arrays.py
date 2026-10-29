#!/usr/bin/env python3
original = [2, 8, 9, 48, 8, 22, -12, 2]
new = [] 

for i in original:
    if i > 5:
        new.append(i + 2)
nnew = set(new)

print(original)
print(nnew)