# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda self, other: self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        cur = res = ListNode()
        min_heap = []

        for head in lists:
            if head:
                heapq.heappush(min_heap, head)

        while min_heap:
            cur.next = (node := heapq.heappop(min_heap))
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, node.next)

        return res.next