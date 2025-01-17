def solution(s):
    answer = []
    for char in s.split():
        if char != "Z":
            answer.append(int(char))
        else:
            if answer:
                answer.pop()
                
    return sum(answer)