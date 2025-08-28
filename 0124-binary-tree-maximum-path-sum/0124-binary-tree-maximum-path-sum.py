# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       self.max_sum = float('-inf')   # global maximum path sum

       def dfs(node):
            if not node:
                return 0

            # Compute max path sum starting from left and right children
            left = max(dfs(node.left), 0)   # ignore negative paths
            right = max(dfs(node.right), 0) # ignore negative paths

            # Case 1: Path passes through this node (including left + right)
            self.max_sum = max(self.max_sum, node.val + left + right)

            # Case 2: For recursion, return the best single path (left OR right + node)
            return node.val + max(left, right)

       dfs(root)
       return self.max_sum
        

        