import math
import os
import random
import re
import sys

def camelcase(s):
    count_uppercase = 0
    for i in s:
        if i.isupper() == True:
            count_uppercase += 1
    return count_uppercase + 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
