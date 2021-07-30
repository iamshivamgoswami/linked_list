from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        h = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(h, [lists[i].val, i])
                lists[i] = lists[i].next

        head = p = ListNode()
        while h:
            v, i = heappop(h)
            p.next = ListNode(v)
            p = p.next
            if lists[i]:
                heappush(h, [lists[i].val, i])
                lists[i] = lists[i].next

        return head.next