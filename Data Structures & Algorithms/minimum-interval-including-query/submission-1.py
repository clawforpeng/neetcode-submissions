class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sols = {}
        intervals.sort()

        q = sorted(queries)

        i = 0
        heap = []

        for query in q:
            # Add everything that has started
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            # Remove everything that already ended
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            if heap:
                sols[query] = heap[0][0]
            else:
                sols[query] = -1
            

        return [sols[q] for q in queries]