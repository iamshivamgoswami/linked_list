class Solution:
    def middleNode(self, head):
        slow, fast = head
        while fast and fast.next:
            slow = slow.nect
            fast = fast.next.next

        return slow
