# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        target = length - n

        if target == 0:
            return head.next
        
        cur = head
        prev = head
        i = 0
        while i < target and cur:
            prev = cur
            cur = cur.next
            i += 1
        
        if cur:
            prev.next = cur.next 
        else:
            prev.next = None
        
        return head