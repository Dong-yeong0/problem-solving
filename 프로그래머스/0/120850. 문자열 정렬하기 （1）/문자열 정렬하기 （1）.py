def solution(my_string):
    count = [0] * 10
    for char in my_string:
        if char.isdigit():
            count[int(char)] += 1
            
    answer = []
    for num in range(10):
        answer.extend([num] * count[num])
    
    return answer
