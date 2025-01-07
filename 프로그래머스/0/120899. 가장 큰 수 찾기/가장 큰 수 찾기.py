"""
def solution(array):
    max_number = array[0]
    answer = [max_number, 0]
    for i, num in enumerate(array):
        if max_number < num:
            max_number = num
            answer = [num, i]
           	           
    return answer
"""

def solution(array):
    max_num = max(array)
    return [max_num, array.index(max_num)]