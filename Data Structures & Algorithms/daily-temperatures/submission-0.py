class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 30
        # 38
        # 30,2 38,1
        # 36,3 38,1
        # 35,4 36,3 38,1
        # 40,5
        # 28,6 40,5
        results = [0] * len(temperatures)
        minHeap = []

        for idx, temp in enumerate(temperatures):
            while minHeap and temp > minHeap[0][0]:
                prev = heapq.heappop(minHeap)
                results[prev[1]] = idx - prev[1]
            heapq.heappush(minHeap, (temp, idx))

        return results