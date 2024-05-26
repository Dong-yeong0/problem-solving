def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        num_str = str(num)
        if all(char in ['0', '5'] for char in num_str):
            answer.append(num)
    return answer if answer else [-1]