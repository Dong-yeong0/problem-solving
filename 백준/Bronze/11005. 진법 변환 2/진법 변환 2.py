def convert_to_base(N, B):    
    digits = []
    while N > 0:
        remainder = N % B
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('A')))
        N //= B
    
    return ''.join(reversed(digits))

N, B = map(int, input().split())
print(convert_to_base(N, B))