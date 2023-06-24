#!/bin/python3

import math
import os
import random
import re
import string
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s: str):
    letters = list(string.ascii_lowercase)
    letters.append(' ')
    s = s.lower()
    for letter in letters:
        if not letter in s:
            return 'not pangram'
    return 'pangram'

    return s
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = 'We promptly judged antique ivory buckles for the next prize'
    result = pangrams(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
