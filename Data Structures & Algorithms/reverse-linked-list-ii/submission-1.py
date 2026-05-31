# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev = dummy = ListNode(0, head)

        for _ in repeat(None, left - 1):
            prev = prev.next

        cur = prev.next

        for _ in repeat(None, right - left):
            temp = cur.next
            cur.next, temp.next, prev.next = temp.next, prev.next, temp

        return dummy.next