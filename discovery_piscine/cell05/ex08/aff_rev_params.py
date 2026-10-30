#!/usr/bin/env python3
import sys
n = (sys.argv[1:])

if n != 0:
     print(" ".join(n[::-1]))
else:
    print("none")