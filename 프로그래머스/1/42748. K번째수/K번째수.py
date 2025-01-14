def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced_sorted = sorted(array[i-1:j])
        answer.append(sliced_sorted[k-1])
    
    return answer