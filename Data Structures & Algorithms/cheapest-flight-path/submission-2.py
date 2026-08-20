class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # sol = 0
        flightsMap = {}
        for flight in flights:
            if flight[0] in flightsMap:
                flightsMap[flight[0]].append((flight[1], flight[2]))
            else:
                flightsMap[flight[0]] = [(flight[1], flight[2])]
        
        dp = [[-2] * (k + 1) for _ in range(n)]
        
        def dfs(i: int, visited: Set[int], stopsLeft: int) -> int:
            if i == dst:
                return 0
            if i in visited or stopsLeft < 0:
                return -1
            
            if dp[i][stopsLeft] != -2:
                return dp[i][stopsLeft]
            
            if not i in flightsMap:
                return -1
            
            visited.add(i)

            minCost = -1

            for flight in flightsMap[i]:
                curCost = dfs(flight[0], visited, stopsLeft - 1)
                cost = flight[1]
                if curCost != -1:
                    if minCost == -1:
                        minCost = cost + curCost
                    else:
                        minCost = min(minCost, cost + curCost)
            
            visited.remove(i)

            dp[i][stopsLeft] = minCost
            return minCost

        return dfs(src, set(), k)