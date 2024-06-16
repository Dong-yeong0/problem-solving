def solution(arr, intervals):
    a1, b1 = intervals[0]
    first_segment = arr[a1:b1 + 1]
    
    a2, b2 = intervals[1]
    second_segment = arr[a2:b2 + 1]
    
    return first_segment + second_segment