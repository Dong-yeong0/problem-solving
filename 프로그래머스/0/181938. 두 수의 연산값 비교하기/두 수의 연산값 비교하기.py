def solution(a, b):
    ab = int(str(a) + str(b))
    _2ab = 2 * a * b
    return max(ab, _2ab)