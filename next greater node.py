# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        def reverse(node, prev=None):
            if not node:
                return prev
            tmp = node.next
            node.next = prev
            return reverse(tmp, node)

        new_list = reverse(head)
        ans = []
        stack = []
        while new_list:
            if len(stack) == 0:
                ans.append(0)
            elif len(stack) > 0 and new_list.val < stack[-1]:

                ans.append(stack[-1])
            elif len(stack) > 0 and new_list.val >= stack[-1]:
                while stack and stack[-1] <= new_list.val:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(0)
                else:
                    ans.append(stack[-1])
            stack.append(new_list.val)
            new_list=new_list.next
        return ans[::-1]




