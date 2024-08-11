def solution(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(s, e + 1):
            if k != 0 and i % k == 0:
                arr[i] += 1
        
    return arr