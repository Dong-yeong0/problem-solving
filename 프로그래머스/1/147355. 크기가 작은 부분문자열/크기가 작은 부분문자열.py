def solution(t, p):
    p_len = len(p)
    answer = 0
    for i in range(len(t) - p_len + 1):
        substr = t[i:i+p_len]
        if int(substr) <= int(p):
            answer += 1
            
    return answer