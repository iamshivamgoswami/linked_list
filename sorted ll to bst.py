# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def func(left=0, right=len(arr) - 1):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(arr[mid])
            root.left = func(left, mid - 1)
            root.right = func(mid + 1, right)

            return root

        return func()
