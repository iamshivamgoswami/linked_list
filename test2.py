# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        left,right=head,head
        stop=False
        def recurse_and_reverse(right,m,n):
            nonlocal left,right
            if n==1:
                return
            right=right.next
            if m>1:
                left=left.next
            recurse_and_reverse(right,m-1,n-1)
            if left==right or right.next==left:
                stop=True
            if not stop:
                left.val,right.val=right.val,left.val

                left=left.next

        recurse_and_reverse(right,m,n)
        return head
