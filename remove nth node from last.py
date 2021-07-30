class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None

        def l(node):
            if not node:
                return 0
            return 1 + l(node.next)

        le = l(head)
        if l == n:
            return head.next
        n = l - n + 1

        def func(node, prev=None):
            nonlocal n
            if not node:
                return
            n -= 1
            if n == 0:
                prev.next = node.next
            func(node.next, node)

        func(head)
        return head
