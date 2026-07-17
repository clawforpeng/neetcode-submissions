"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        built = {} # completed nodes
        newNodes = {} # initalized nodes

        queue = deque() # node to visit (old nodes)
        queue.append(node)
        root = None

        while queue:
            n = queue.popleft()
            if n.val in built:
                continue

            cur = Node(n.val)
            if n.val in newNodes:
                cur = newNodes[n.val]
            else:
                newNodes[n.val] = cur

            for neighbor in n.neighbors:
                if neighbor.val in newNodes:
                    cur.neighbors.append(newNodes[neighbor.val])
                else:
                    newNeighbor = Node(neighbor.val)
                    newNodes[neighbor.val] = newNeighbor
                    cur.neighbors.append(newNeighbor)
            
            built[n.val] = True

            for neighbor in n.neighbors:
                if neighbor.val not in built:
                    queue.append(neighbor)

            if cur.val == 1:
                root = cur
        return root