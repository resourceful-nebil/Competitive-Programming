# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        def dfs(root,curSum):
            nonlocal cnt
            if not root:
                return
            
            curSum += root.val
            if curSum == targetSum:
                cnt += 1
            
            dfs(root.right,curSum)
            dfs(root.left,curSum)
        
        def traverse(root):
            if not root:
                return 
            
            dfs(root,0)
            traverse(root.left)
            traverse(root.right)


        
        traverse(root)
        return cnt