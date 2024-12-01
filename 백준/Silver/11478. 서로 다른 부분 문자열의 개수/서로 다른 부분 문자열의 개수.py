import sys


def count_unique_substrings(s: str) -> int:
    unique_substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            unique_substrings.add(s[i:j])

    return len(unique_substrings)


S = str(sys.stdin.readline().strip())
print(count_unique_substrings(S))
