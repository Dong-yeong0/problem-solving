def solution(arr):
    for idx, num in enumerate(arr):
        if num >= 50 and num & 1 == 0:
            arr[idx] /= 2
        elif num <= 50 and num & 1 != 0:
            arr[idx] *= 2
    return arr