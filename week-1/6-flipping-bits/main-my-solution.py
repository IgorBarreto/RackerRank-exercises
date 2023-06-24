#!/bin/python3

import math
import os
import random
import re
import sys


def decimal_to_binary(number):
    result = [0] * 32
    start = 1
    while number >= 1:
        if number % 2 == 0:
            result[32 - start] = 0
        else:
            result[32 - start] = 1
        number //= 2
        start += 1
    return [str(r) for r in result]


def binary_to_decimal(number):
    number = number[::-1]
    r = 0
    for index, n in enumerate(number):
        r += int(n) * (2**index)
    return r


def invert_digits(number):
    return ['1' if i == '0' else '0' for i in number]


def flippingBits(n):
    result = decimal_to_binary(n)
    result = invert_digits(result)
    result = binary_to_decimal(result)
    return result


if __name__ == '__main__':
    fptr = open('./6-flipping-bits/output.txt', 'w')

    for q_itr in q:
        n = int(q_itr)

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
