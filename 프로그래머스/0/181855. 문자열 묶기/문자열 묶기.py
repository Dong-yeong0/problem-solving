def solution(str_arr):
    answer = {}
    for char in str_arr:
        length = len(char)
        if length in answer:
            answer[length] += 1
        else:
            answer[length] = 1
    
    return max(answer.values())