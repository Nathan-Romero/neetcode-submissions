# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next, slow = None, slow.next
        prev = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        while prev:
            head.next, head = prev, head.next
            prev.next, prev = head, prev.next