#!/bin/python3

import math
import os
import random
import re
import sys


def flippingBits(n):
    # Write your code here
    bin_str = f'{n:032b}'
    out = "".join(["0" if i == "1" else "1" for i in bin_str])
    return int(out, 2)


if __name__ == '__main__':
    fptr = open('./6-flipping-bits/output.txt', 'w')

    # q = ['2147483647', '1', '0']
    q = ['2147483647']
    for q_itr in q:
        n = int(q_itr)

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
