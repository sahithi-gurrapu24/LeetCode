# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        def traversal(root,arr):
            if root==None:
                return
            traversal(root.left,arr)
            arr.append(root.val)
            traversal(root.right,arr)
        traversal(p,arr1)
        traversal(q,arr2)
        if arr1==arr2:
            return True
        return False

        