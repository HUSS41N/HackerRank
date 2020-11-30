import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    tallest_candle = max(candles)
    number_of_tallest_candle = 0 
    for i in candles:
        if i == tallest_candle:
            number_of_tallest_candle += 1
    return number_of_tallest_candle

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
