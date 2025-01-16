"""
def solution(before, after):
    return 1 if "".join(reversed(before)) == after else 0
"""

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0