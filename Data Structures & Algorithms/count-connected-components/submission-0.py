class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        unvisited = set()
        adjList = {}
        for i in range(n):
            unvisited.add(i)
            adjList[i] = []
        
        for edge in edges:
            a = edge[0]
            b = edge[1]
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node: int):
            if node not in unvisited:
                return
            unvisited.remove(node)

            neighbors = adjList[node]

            for neighbor in neighbors:
                dfs(neighbor)
        
        while unvisited:
            root = unvisited.pop()
            unvisited.add(root)
            count += 1
            dfs(root)

        return count