def solution(a, b, c, d):
    num_list = [a, b, c, d]
    freq = {}
    for num in num_list:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    case = len(freq)
    if case == 1:
        p = list(freq)[0]
        return 1_111 * p
    elif case == 2:
        values = list(freq.values())
        keys = list(freq.keys())
        if 3 in values:
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        else:
            p, q = keys
            return (p + q) * abs(p - q)
    elif case == 3:
        keys = [k for k, v in freq.items() if v == 1]
        q, r = keys
        return q * r
    else:
        return min(num_list)