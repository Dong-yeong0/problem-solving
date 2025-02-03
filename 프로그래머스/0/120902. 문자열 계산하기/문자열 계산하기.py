def solution(my_string):
    elements = my_string.split()
    result = int(elements[0])
    for i in range(1, len(elements), 2):
        operator = elements[i]
        num = int(elements[i + 1])
        if operator == '+':
            result += num
        else:
            result -= num
    
    return result