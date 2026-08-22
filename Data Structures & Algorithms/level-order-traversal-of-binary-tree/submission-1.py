# TC : O(n) We visit every node exactly once. SC : O(n) because queue upto n values and res can hold all n node values. If excluding output space, auxiliary space is O(n) because of the queue.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        
        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(level)
        return res
        