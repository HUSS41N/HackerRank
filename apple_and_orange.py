import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [x+a for x in apples]
    oranges = [x+b for x in oranges]
    count_apples = 0
    count_oranges = 0
    for i in apples:
        if i in range(s,t):
            count_apples += 1
    for i in oranges:
        if i in range(s,t):
            count_oranges += 1
    print(count_apples)
    print(count_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
