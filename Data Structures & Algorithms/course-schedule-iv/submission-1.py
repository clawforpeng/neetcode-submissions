class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        sols = []

        memo = [[0] * numCourses for _ in range(numCourses)]

        for prereq in prerequisites:
            a = prereq[0]
            b = prereq[1]

            if b not in adjList:
                adjList[b] = set()
            adjList[b].add(a)

        def dfs(start: int, end: int) -> bool:
            if memo[start][end] != 0:
                return memo[start][end] == 1
            if start not in adjList:
                memo[start][end] = -1
                return False
            prereqs = adjList[start]

            if end in prereqs:
                memo[start][end] = 1
                return True
            
            for prereq in prereqs:
                if dfs(prereq, end):
                    memo[start][end] = 1
                    return True
            
            memo[start][end] = -1
            return False

        for query in queries:
            u = query[0]
            v = query[1]

            sols.append(dfs(v, u))
        
        return sols
