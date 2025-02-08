def solution(picture, k):
    answer = []
    for row in picture:
        enlarged_row = ''.join(char * k for char in row)
        for _ in range(k):
            answer.append(enlarged_row)
            
    return answer