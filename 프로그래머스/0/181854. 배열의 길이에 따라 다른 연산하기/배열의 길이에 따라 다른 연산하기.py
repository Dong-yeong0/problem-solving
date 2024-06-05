def solution(arr, n):
    arr_len = len(arr)
    if arr_len % 2 == 0:
        arr[1::2] = [x + n for x in arr[1::2]]
    else:
        arr[0::2] = [x + n for x in arr[0::2]]
    return arr
