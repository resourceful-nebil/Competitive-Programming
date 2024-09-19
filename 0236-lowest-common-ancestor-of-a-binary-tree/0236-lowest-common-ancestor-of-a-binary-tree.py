# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if not root or root == p or root == q:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            return root if (right and left) else (left or right)
        
        return dfs(root)