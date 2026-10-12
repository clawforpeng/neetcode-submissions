class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, point[0], point[1]))
            else:
                if dist < -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist, point[0], point[1]))
        
        sols = []

        while maxHeap:
            point = heapq.heappop(maxHeap)
            sols.append([point[1], point[2]])
        
        return sols