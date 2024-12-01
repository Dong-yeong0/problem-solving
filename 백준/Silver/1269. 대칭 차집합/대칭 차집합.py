import sys

A, B = list(map(int, sys.stdin.readline().split()))
a_elements = set(map(int, sys.stdin.readline().split()))
b_elements = set(map(int, sys.stdin.readline().split()))
a_difference = a_elements - b_elements
b_difference = b_elements - a_elements
print(len(a_difference) + len(b_difference))