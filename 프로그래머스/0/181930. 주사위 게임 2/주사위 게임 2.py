def solution(a, b, c):
    answer = 0
    if a != b != c:
        answer = a + b + c
    if a == b != c or a == c != b or b == c != a:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    if a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    return answer