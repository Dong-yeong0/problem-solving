# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        current_node = head.next
        sum_value = 0
        while current_node:
            if current_node.val == 0:
                if sum_value > 0:
                    current.next = ListNode(sum_value)
                    current = current.next
                    sum_value = 0
            else:
                sum_value += current_node.val
            current_node = current_node.next

        return dummy.next