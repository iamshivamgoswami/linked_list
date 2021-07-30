# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def func(node,prev=None):
            if not node:
                return prev
            new_node=node.next
            node.next=prev
            return func(new_node,node)
        return func(head)