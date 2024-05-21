def solution(a, b):
    a_str, b_str = str(a), str(b)
    ab = int(a_str + b_str)
    ba = int(b_str + a_str)
    return max(ab, ba)