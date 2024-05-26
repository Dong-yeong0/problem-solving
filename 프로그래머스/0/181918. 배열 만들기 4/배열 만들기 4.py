def solution(arr):
    stk = []
    for num in arr:
        if not stk:
            stk.append(num)
        else:
            while stk and stk[-1] >= num:
                stk.pop()
            stk.append(num)
    return stk