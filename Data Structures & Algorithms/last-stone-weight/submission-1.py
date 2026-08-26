class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * (-1) for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            if a < b:
                heapq.heappush(stones, a - b)
        
        if len(stones) == 1:
            return -stones[0]
        return 0