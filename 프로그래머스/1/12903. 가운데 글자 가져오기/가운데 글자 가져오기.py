def solution(s):
    s_len = len(s)
    half = s_len // 2
    return s[half-1:half+1] if s_len % 2 == 0 else s[half]
