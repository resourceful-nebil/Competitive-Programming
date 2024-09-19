# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node, isLeft, length):
            nonlocal longest
            if not node:
                return

            longest = max(longest, length)
            
            if isLeft:
                dfs(node.right,False,length + 1)
                dfs(node.left, True,1)  
            else:
                dfs(node.left,True,length+1)
                dfs(node.right,False, 1)
        
        dfs(root.left,True,1)
        dfs(root.right,False,1)
        return longest
