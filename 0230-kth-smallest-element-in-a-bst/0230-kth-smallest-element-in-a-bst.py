# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        sorted(arr)
        return arr[k-1]

       

        