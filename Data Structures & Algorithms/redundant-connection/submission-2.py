class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphs = {}
        paths = set()
        visited = set()

        for a, b in edges:
            graphs.setdefault(a, []).append(b)
            graphs.setdefault(b, []).append(a)

        cycleStart = -1

        def dfs(prev, cur):
            nonlocal cycleStart

            if cur in visited:
                cycleStart = cur
                return True

            visited.add(cur)

            for nei in graphs[cur]:
                if nei == prev:
                    continue

                if dfs(cur, nei):
                    if cycleStart != -1:
                        paths.add(cur)

                    if cur == cycleStart:
                        cycleStart = -1

                    return True

            return False

        dfs(-1, 1)

        for a, b in reversed(edges):
            if a in paths and b in paths:
                return [a, b]

        return []