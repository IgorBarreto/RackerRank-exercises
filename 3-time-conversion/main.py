#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    am_pm = s[-2:].lower()
    time_hour = s[:-2].split(':')
    if am_pm == 'am':
        if time_hour[0] == '12':
            time_hour[0] = '00'
    else:
        if time_hour[0] != '12':
            time_hour[0] = str(int(time_hour[0]) + 12)
    return ':'.join(time_hour)


if __name__ == '__main__':
    # fptr = open('./3-time-conversion/output.txt', 'w+')

    # s = input()
    # s = '07:05:45PM'
    s = '12:45:54PM'

    result = timeConversion(s)
    print(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
