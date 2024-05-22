def solution(ineq, eq, n, m):
    answer = {
        (">", "="): lambda n, m: n >= m,
        ("<", "="): lambda n, m: n <= m,
        (">", "!"): lambda n, m: n > m,
        ("<", "!"): lambda n, m: n < m
    }
    return 1 if answer[(ineq, eq)](n, m) else 0