def solution(arr: list) -> list:
    stk = []
    for i in range(len(arr)):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop(-1)
            i += 1
        elif stk and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
            
    return stk if stk else [-1]