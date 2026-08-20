# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sol = ListNode(-1)

        minHeap = []

        for index, li in enumerate(lists):
            if li:
                heapq.heappush(minHeap, (li.val, index, li))
        
        prev = sol
        while minHeap:
            # targetIndex = -1
            curNodeTuple = heapq.heappop(minHeap)
            curNode = curNodeTuple[2]

            # for index, li in enumerate(lists):
            #     if not curNode or (li and li.val < curNode.val):
            #         curNode = li
            #         targetIndex = index
            
            
            prev.next = curNode
            prev = prev.next
            
            ne = curNode.next
            curNode.next = None

            if ne:
                heapq.heappush(minHeap, (ne.val, curNodeTuple[1], ne ))
            
            
        return sol.next