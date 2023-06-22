def miniMaxSum(arr):
    sum_arr = sum(arr)
    min_value = max_value = sum(arr[0:4])
    for item in arr:
        temp = sum_arr - item
        if temp < min_value:
            min_value = temp
        if temp > max_value:
            max_value = temp
    print(f'{min_value} {max_value}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
