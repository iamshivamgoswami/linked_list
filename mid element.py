# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def le(node):
            if not node:
                return 0
            return 1 + le(node.next)

        mid = le(head) // 2 + 1

        while head:
            mid -= 1
            if mid == 0:
                return head
            head = head.next


