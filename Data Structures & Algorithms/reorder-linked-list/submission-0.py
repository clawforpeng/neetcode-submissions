# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        slow = head
        fast = head.next

        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        if slow and not slow.next:
            return

        secondList = slow.next
        slow.next = None
        prev = None
        curr = secondList

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        first = head
        second = prev
        while first and second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext

        # 1 2 3 -> 1 3 2.     