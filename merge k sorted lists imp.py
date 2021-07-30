# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h=[]
        for i in range(len(lists)):
            if lists[i]:

                heapq.heappush(h,(lists[i].val,i))
                lists[i]=lists[i].next

        dummy=p=ListNode(-1)
        while h:
            v,i=heapq.heappop(h)
            p.next=ListNode(v)
            p=p.next
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i))
                lists[i]=lists[i].next

        return dummy.next

