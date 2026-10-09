class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        minHeap = []

        for val, count in counts.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (count, val))
            else:
                if count > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (count, val))
        
        sol = []

        for h in minHeap:
            sol.append(h[1])
        
        return sol