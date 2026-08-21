# Time Complexity: O(n) We visit every node exactly once. Space Complexity: O(h) (recursion depth) Worst case: O(n) for skewed tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0, True

            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            height = 1 + max(left_height, right_height)
            
            balanced = (
                left_balanced and 
                right_balanced and
            abs(left_height - right_height)<= 1
            )

            return height, balanced
        return dfs(root)[1]