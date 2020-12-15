#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    arr = []
    for word in s:
        if word not in arr:
            arr.append(word)
        else:
            if arr[-1] == word:
                arr.pop()
            else:
                arr.append(word)
    if len(arr) == 0:
        return 'Empty String'
    else:
        return ''.join(arr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
