#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = []
    negative = []
    zero = []
    for i in arr:
        if i == 0:
            zero.append(i)
        elif i > 0:
            positive.append(i)
        elif 0 > i:
            negative.append(i)
    x = len(positive)/len(arr)
    y = len(negative)/len(arr)
    z = len(zero)/len(arr)
    print(x)
    print(y)
    print(z)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
