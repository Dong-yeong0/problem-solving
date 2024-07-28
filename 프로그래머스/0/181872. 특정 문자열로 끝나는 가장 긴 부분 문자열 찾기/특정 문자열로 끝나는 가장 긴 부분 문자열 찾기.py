def solution(myString, pat):
    last_index = myString.rfind(pat)
    if last_index != -1:
        return myString[:last_index + len(pat)]
        
    return ''
