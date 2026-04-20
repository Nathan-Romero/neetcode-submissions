# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second portion of the list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next   # Temporarily store the next node
            second.next = prev  # Set cur node to point to previous node
            prev = second       # Shift prev pointer one step forward to the current node
            second = tmp        # Shift cur pointer one step forward to the next node (stored in tmp)

        # merge two halves
        first, second = head, prev  # after previous while loop, second = None, prev = last pointer in 2nd half of list (n-1)
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2