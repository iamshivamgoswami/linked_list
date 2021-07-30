class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        def reverse(node, prev=None):
            if not node:
                return prev
            new_node = node.next
            node.next = prev
            return reverse(new_node, node)

        head2 = reverse(slow)
        while head2:
            if head.val != head2.val:
                return False
            head2 = head2.next
            head = head.next
        return True
