def solution(myStr):
    answer = []
    current_substr = ""
    for char in myStr:
        if char in "abc":
            if current_substr:
                answer.append(current_substr)
                current_substr = ""
        else:
            current_substr += char
    
    if current_substr:
        answer.append(current_substr)
    
    return answer if answer else ["EMPTY"]