# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node, prev=None):
            if not node:
                return prev
            new_node = node.next
            node.next = prev
            return reverse(new_node, node)

        first, second = head, reverse(slow)
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


