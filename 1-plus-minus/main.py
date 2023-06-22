import math
import os
import random
import re
import sys


def plusMinus(arr):
    length = len(arr)
    greater_than_zero = 0
    lesser_than_zero = 0
    zero = 0
    for item in arr:
        if item > 0:
            greater_than_zero += 1
        elif item < 0:
            lesser_than_zero += 1
        else:
            zero += 1
    print(f'{greater_than_zero / length:.6f}')
    print(f'{lesser_than_zero / length:.6f}')
    print(f'{zero / length:.6f}')


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
