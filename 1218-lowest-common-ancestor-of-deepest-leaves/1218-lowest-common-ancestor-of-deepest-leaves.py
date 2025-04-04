# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #return(LCA,height)
        def dfs(node):
            if not node:
                return (node,0)
            
            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height > right_height:
                return (left_node, left_height + 1)
            elif right_height > left_height:
                return (right_node, right_height + 1)
            return (node, left_height + 1)
        
        res, _ = dfs(root)
        return res
            