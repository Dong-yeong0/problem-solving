def solution(arr):
    n = len(arr)
    factor = 1
    while factor < n:
        factor *= 2
        
    return arr + [0] * (factor - n)