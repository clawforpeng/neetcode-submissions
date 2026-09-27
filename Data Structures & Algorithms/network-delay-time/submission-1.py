class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTime = [math.inf] * (n + 1)

        adjList = {}

        for time in times:
            source = time[0]
            target = time[1]
            ti = time[2]

            if source not in adjList:
                adjList[source] = []
            
            adjList[source].append((target, ti))
        
        def dfs(cur: int, dis: int):
            if dis >= minTime[cur]:
                return
            minTime[cur] = dis
            if cur not in adjList:
                return
            for neighbor in adjList[cur]:
                dfs(neighbor[0], dis + neighbor[1])
        
        dfs(k, 0)
        sol = 0

        for i in range(1, n + 1):
            if minTime[i] == math.inf:
                return -1
            sol = max(sol, minTime[i])
        
        return int(sol)