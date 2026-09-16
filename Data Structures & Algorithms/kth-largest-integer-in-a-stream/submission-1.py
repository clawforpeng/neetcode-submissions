class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap, num)
            else:
                top = self.minHeap[0]
                if top < num:
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            top = self.minHeap[0]
            if top < val:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        
        return self.minHeap[0]