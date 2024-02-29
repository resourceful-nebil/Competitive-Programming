# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if not right and not left:
                return True 
            
            if not right or not left:
                return False
            
            # left,right = dfs(left,right)

            return (right.val == left.val and dfs(left.left,right.right) and dfs(left.right,right.left))

        
        return dfs(root.left,root.right)