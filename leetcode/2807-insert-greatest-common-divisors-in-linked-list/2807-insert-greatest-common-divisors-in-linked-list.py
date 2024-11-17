# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(a: int, b: int):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            g = gcd(current.val, current.next.val)
            new_node = ListNode(g)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        return head 