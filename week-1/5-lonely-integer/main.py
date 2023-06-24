# Complete the 'lonely_integer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonely_integer(a: list):
    for item in a:
        if a.count(item) == 1:
            return item


if __name__ == '__main__':
    fptr = open('./5-lonely-integer/output.txt', 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    result = lonely_integer(a)

    fptr.write(str(result) + '\n')

    fptr.close()
