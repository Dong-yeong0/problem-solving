def solution(arr, k):
    operation = lambda x: x * k if k % 2 else x + k
    return list(map(operation, arr))
