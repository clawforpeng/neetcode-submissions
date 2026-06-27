# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 none
# 1->2->3 0->None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        cur = head

        while cur is not None:
            next = cur.next
            old = newHead
            newHead = cur
            newHead.next = old
            cur = next
        
        return newHead