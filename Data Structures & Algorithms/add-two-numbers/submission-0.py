# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol = ListNode(-1)
        cur = sol

        carry = 0
        while l1 and l2:
            agg = l1.val + l2.val + carry

            if agg > 9:
                carry = 1
                cur.next = ListNode(agg - 10)
            else:
                carry = 0
                cur.next = ListNode(agg)
            
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        while l1:
            agg = l1.val + carry
            if agg > 9:
                carry = 1
                cur.next = ListNode(agg - 10)
            else:
                carry = 0
                cur.next = ListNode(agg)
            cur = cur.next
            l1 = l1.next

        while l2:
            agg = l2.val + carry
            if agg > 9:
                carry = 1
                cur.next = ListNode(agg - 10)
            else:
                carry = 0
                cur.next = ListNode(agg)
            cur = cur.next
            l2 = l2.next

        if carry == 1:
            cur.next = ListNode(1)
        
        return sol.next