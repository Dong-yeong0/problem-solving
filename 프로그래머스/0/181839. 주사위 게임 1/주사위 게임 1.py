def solution(a, b):
    if a % 2 == b % 2:
        return a ** 2 + b ** 2 if a % 2 != 0 else abs(a - b)
    else:
        return 2 * (a + b)
