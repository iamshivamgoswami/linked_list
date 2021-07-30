# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        n = dummy
        if not head:
            return

        odd = even = head
        while odd:

            n.next = ListNode(odd.val)
            n = n.next
            if not odd.next:
                break
            odd = odd.next.next

        m = dummy2 = ListNode(-1)
        even = even.next
        while even:
            m.next = ListNode(even.val)
            m = m.next
            if not even.next:
                break
            even = even.next.next

        n.next = dummy2.next
        return dummy.next

