import sys

count = 0
N = int(sys.stdin.readline())
stack = []
while count < N:
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print((-1))
    elif command[0] == 3:
        print((len(stack)))
    elif command[0] == 4:
        print(int(bool(not stack)))
    elif command[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print((-1))
    
    count += 1
