class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        visited = {}

        for i in range(n):
            adjList[i] = []
            visited[i] = False
        
        for edge in edges:
            a = edge[0]
            b = edge[1]

            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(node: int, parent: int) -> bool:
            if visited[node]:
                return False
            
            visited[node] = True

            if len(adjList[node]) == 1:
                if parent == adjList[node][0]:
                    return True
                else:
                    return dfs(adjList[node][0], node)
            
            sol = True
            for neighbor in adjList[node]:
                if neighbor != parent:
                    sol = sol and dfs(neighbor, node)
            
            return sol
        
        if not dfs(0, -1):
            return False
        
        for key in visited:
            if not visited[key]:
                return False
        
        return True
