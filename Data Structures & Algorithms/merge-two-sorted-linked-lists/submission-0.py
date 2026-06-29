# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        newHead = None
        cur = None

        # merge two list
        while head1 and head2:
            if not newHead:
                if head1.val <= head2.val:
                    newHead = head1
                    head1 = head1.next
                else:
                    newHead = head2
                    head2 = head2.next
            else:
                if not cur:
                    cur = newHead

                if head1.val <= head2.val:
                    cur.next = head1
                    cur = cur.next
                    head1 = head1.next
                else:
                    cur.next = head2
                    cur = cur.next
                    head2 = head2.next

        if head1:
            if not newHead:
                newHead = head1
            else:
                if not cur:
                    cur = newHead
                cur.next = head1
        
        if head2:
            if not newHead:
                newHead = head2
            else:
                if not cur:
                    cur = newHead
                cur.next = head2
            
        return newHead