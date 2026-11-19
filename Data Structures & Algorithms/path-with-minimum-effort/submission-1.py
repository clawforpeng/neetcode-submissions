class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        memo = [[float('inf')] * len(heights[0]) for _ in range(len(heights))]

        minHeap = []

        memo[0][0] = 0

        heapq.heappush(minHeap, (0, 0, 0))

        while minHeap:
            node = heapq.heappop(minHeap)
            val = node[0]

            i = node[1]
            j = node[2]

            if val > memo[i][j]:
                continue
            
            cur = heights[i][j]

            if i > 0 and memo[i - 1][j] > max(val, abs(heights[i - 1][j] - cur)):
                memo[i - 1][j] = max(val, abs(heights[i - 1][j] - cur))
                heapq.heappush(minHeap, [memo[i - 1][j], i - 1, j])
            if i + 1 < len(heights) and memo[i + 1][j] > max(val, abs(heights[i + 1][j] - cur)):
                memo[i + 1][j] = max(val, abs(heights[i + 1][j] - cur))
                heapq.heappush(minHeap, [memo[i + 1][j] , i + 1, j])
            if j > 0 and memo[i][j - 1] > max(val, abs(heights[i][j - 1] - cur)):
                memo[i][j - 1] = max(val, abs(heights[i][j - 1] - cur))
                heapq.heappush(minHeap, [memo[i][j - 1], i, j - 1])
            if j + 1 < len(heights[0]) and memo[i][j + 1] > max(val, abs(heights[i][j + 1] - cur)):
                memo[i][j + 1] = max(val, abs(heights[i][j + 1] - cur))
                heapq.heappush(minHeap, [memo[i][j + 1], i, j + 1])
        
        return int(memo[-1][-1])
            
            
                