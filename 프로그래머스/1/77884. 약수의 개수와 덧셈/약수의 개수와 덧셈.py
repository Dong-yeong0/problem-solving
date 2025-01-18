"""
def getDivisors(n):
    result = []
    for i in range(1, int(n ** (1/2) + 1)):
        if n % i == 0:
            result.append(i)
            if ((i ** 2) != n):
                result.append(n // i)
                
    result.sort()
    return result      

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisors = getDivisors(i)
        if len(divisors) % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer
"""

# 완전제곱수(약수의 갯수가 홀수 인 경우)로 접근
def is_perfect_number(n):
    return int(n ** 0.5) ** 2 == n

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if is_perfect_number(i):
            answer -= i
        else:
            answer += i
            
    return answer