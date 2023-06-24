import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    primary_diagonal, second_diagonal = 0, 0
    n = len(arr)
    for i in range(n):
        primary_diagonal += arr[i][i]
        second_diagonal += arr[i][n - 1 - i]
    return abs(primary_diagonal - second_diagonal)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    print('F', (11 + 5 + (-12)) - (4 + 5 + 10))
    # arr = [
    #     [11, 2, 4],
    #     [4, 5, 6],
    #     [10, 8, -12],
    # ]
    arr = [
        [-1, 1, -7, -8],
        [-10, -8, -5, -2],
        [0, 9, 7, -1],
        [4, 4, -2, 1],
    ]
    #    arr2 = [
    #        ['00', '01', '02'],
    #        ['10', '11', '12'],
    #        ['20', '21', '22'],
    #    ]
    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
