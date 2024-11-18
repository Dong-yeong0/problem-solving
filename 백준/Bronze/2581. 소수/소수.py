def is_prime_number(number: int):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


N = int(input())
M = int(input())
prime_numbers = set()

for j in range(N, M + 1):
    if is_prime_number(j):
        prime_numbers.add(j)

if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)
