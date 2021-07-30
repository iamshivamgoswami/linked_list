# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        n = dummy  # smaller
        dummy2 = ListNode(-1)
        m = dummy2  # larger
        while head:
            if head.val < x:
                n.next = ListNode(head.val)
                n = n.next
            else:
                m.next = ListNode(head.val)
                m = m.next
            head = head.next
        n.next = dummy2.next
        return dummy.next


