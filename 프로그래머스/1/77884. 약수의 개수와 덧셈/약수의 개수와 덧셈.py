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