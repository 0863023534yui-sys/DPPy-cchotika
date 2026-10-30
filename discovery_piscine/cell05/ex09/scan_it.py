#!/usr/bin/env python3
import sys 
import re 

if len(sys.argv) == 3:
    word = sys.argv[1]
    text = sys.argv[2]
    result = re.findall(re.escape(word), text)
    if result:
        print (len(result))
    else:
        print ("none")
else:
    print ("none")