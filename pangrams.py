import math
import os
import random
import re
import sys

def pangrams(s):
    s = s.replace(' ','').lower()
    s = set(list(s))
    if len(s) == 26:
        return 'pangram'
    else:
        return 'not pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
