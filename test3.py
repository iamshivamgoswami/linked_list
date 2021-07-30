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
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        def reverse(node,prev=None):
            if not node:
                return prev
            new_node=node.next
            node.next=prev
            return reverse(new_node,node)

        second=reverse(slow)
        first=head
        while second.next:
            tmp=first.next
            first.next=second
            first=tmp
            tmp=second.next
            second.next=first
            second=tmp

