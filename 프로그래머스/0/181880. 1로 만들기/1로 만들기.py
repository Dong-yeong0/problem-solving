def solution(num_list):
    answer = 0
    
    for num in num_list:
        operation = 0
        while num != 1:
            if num % 2 == 0:
                num >>= 1
            else:
                num = (num - 1) >> 1
            operation += 1
        answer += operation
    
    return answer