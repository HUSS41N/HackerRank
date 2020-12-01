#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    a = [a[0],a[1],a[2]]
    b = [b[0],b[1],b[2]]
    if a[0]>b[0]:
        alice+=1
    elif b[0] > a[0]:
        bob+= 1
    if a[1]>b[1]:
        alice += 1
    elif b[1] > a[1]:
        bob+= 1
    if a[2]>b[2]:
        alice += 1
    elif b[2] > a[2]:
        bob+= 1
    
    return [alice,bob]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
