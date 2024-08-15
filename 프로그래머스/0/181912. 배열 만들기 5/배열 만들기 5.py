def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        split_num = int(num[s:s+l])
        if split_num > k:
            answer.append(split_num)
            
    return answer