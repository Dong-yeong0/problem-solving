def solution(my_string):
    answer = ""
    for string in my_string:
        if ord("a") > ord(string):
            answer += chr(ord(string) + 32)
        else:
            answer += chr(ord(string) - 32)

    return answer