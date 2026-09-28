class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTime = [math.inf] * (n + 1)
        # minTime[k] = 0

        adjList = {}

        for time in times:
            source = time[0]
            target = time[1]
            ti = time[2]

            if source not in adjList:
                adjList[source] = []
            
            adjList[source].append((ti, target))
        
        minHeap = []
        heapq.heappush(minHeap, (0, k))

        while minHeap:
            no = heapq.heappop(minHeap)

            time = no[0]
            node = no[1]

            if time < minTime[node]:
                minTime[node] = time
                if node in adjList:
                    for neighbor in adjList[node]:
                        heapq.heappush(minHeap, (time + neighbor[0], neighbor[1]))
        
        sol = 0

        for i in range(1, n + 1):
            if minTime[i] == math.inf:
                return -1
            sol = max(sol, minTime[i])
        
        return int(sol)
        