def solution(a, d, included):
    answer = 0
    current_number = a 
    
    for i in range(len(included)):
        if included[i]:
            answer += current_number
        current_number += d
    
    return answer
