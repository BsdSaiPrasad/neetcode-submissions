# For Clone Graph:
# - TC: O(V + E)
#   Each vertex is cloned once, and each edge/neighbor connection is examined once.
# - SC: O(V)
#   HashMap stores one copied node per original node, and recursion stack can be up to O(V) in the worst case.


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

        old_to_new = {}

        def dfs(node):
            
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)



            