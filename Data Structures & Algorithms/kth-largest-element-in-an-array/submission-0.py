class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, -num)

        for _ in range(k - 1):
            heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap) * (-1)