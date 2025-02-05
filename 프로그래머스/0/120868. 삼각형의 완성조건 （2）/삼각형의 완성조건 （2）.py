def solution(sides):
    a, b = sorted(sides)
    min_c = b - a + 1
    max_c = a + b - 1
    return max(0, max_c - min_c + 1)