class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def dfs(cur, target, visited):
            if cur == target:
                return True

            visited.add(cur)

            for nei in graph.get(cur, []):
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for a, b in edges:
            # If a and b are already connected,
            # this edge creates a cycle.
            if a in graph and b in graph:
                if dfs(a, b, set()):
                    return [a, b]

            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)

        return []