def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min_val = float('inf')
        has_found = False
        for i in range(s, e + 1):
            if arr[i] > k:
                min_val = min(min_val, arr[i])
                has_found = True
        if has_found:
            answer.append(min_val)
        else:
            answer.append(-1)
        
    return answer