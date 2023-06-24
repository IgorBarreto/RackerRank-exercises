#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(0, len(s)):
        if i + m < (len(s) + 1):
            if sum(s[i : i + m]) == d:
                count += 1
    return count
    #  s = [2, 2, 1, 3, 2]
    # length subArray = m = 2
    # sum subArray = d = 4
    # results = 2 => [2,2] and [1,3]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    # n = int(input().strip())

    # s = list(map(int, input().rstrip().split()))

    # first_multiple_input = input().rstrip().split()

    # d = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
