def solution(my_strings, parts):
    answer = ''
    for word, (start, end) in zip(my_strings, parts):
        answer += word[start:end + 1]
    return answer