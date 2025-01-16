def solution(array, n):
    closest_num = array[0]
    min_diff = abs(closest_num - n)
    for num in array:
        diff = abs(num - n)
        if diff < min_diff:
            closest_num = num
            min_diff = diff
        elif diff == min_diff:
            closest_num = min(closest_num, num)
            
    return closest_num