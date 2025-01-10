def solution(order):
    answer = 0
    for word in str(order):
        if word in ["3", "6", "9"] :
            answer += 1
            
    return answer