"""
def solution(my_string):
    return "".join(sorted(list(my_string.lower())))
"""

def solution(my_string):
    answer = []
    for char in my_string:
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            answer.append(chr(ord(char) + 32)) # 대문자를 ascii로 바꾸어 32를 더하면 해당 문자의 소문자로 변환이 가능하다.
        else:
            answer.append(char)

    return "".join(sorted(answer))