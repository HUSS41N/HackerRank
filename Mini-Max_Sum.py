import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:4])
    max = sum(arr[1::])
    print(f'{min} {max}')
    
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
