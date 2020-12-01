import os
import sys
def timeConversion(s):
    t = list(range(13,25))
    if s[-2:] == 'AM':
        if s[0:2] == '12':
            return('00'+s[2:-2])
        else:
            return(s[:-2])

    elif s[-2:] == 'PM':
        if s[0:2] == '12':
            return('12'+s[2:-2])
        else:
            return(str(t[int(s[0:2])-1])+s[2:-2])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
