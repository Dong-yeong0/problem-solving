def solution(s):
    answer = 0
    last_cal_num = 0
    for char in s.split():
        if char == "Z":
            answer -= last_cal_num
            continue
            
        num = int(char)
        answer += num
        last_cal_num = num

    return answer