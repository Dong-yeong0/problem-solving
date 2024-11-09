call_count = 0

def recursion(s, l, r):
    global call_count
    call_count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    global call_count
    call_count = 0
    return recursion(s, 0, len(s) - 1)

t = int(input())
for _ in range(t):
    word = input().strip()
    print(isPalindrome(word), call_count)