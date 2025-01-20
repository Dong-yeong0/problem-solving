def solution(n):
    answer = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            answer.add(i)
            n //= i
        i += 1
    
    if n > 1:
        answer.add(n)
    
    return sorted(set(answer))
