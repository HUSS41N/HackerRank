#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    count_minimum = 0
    count_maximum = 0
    for i in range(len(scores)):
        if scores[i] > maximum:
            maximum = scores[i]
            count_maximum += 1
        if scores[i] < minimum:
            minimum = scores[i]
            count_minimum += 1
    return count_maximum,count_minimum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
