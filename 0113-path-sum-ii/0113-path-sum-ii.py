# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        current_path = []
        paths = []

        def dfs(root,curSum):
            if not root:
                return 
            
            curSum += root.val
            current_path.append(root.val)
            if not root.right and not root.left and curSum == targetSum:
                paths.append(current_path[:])
            
            dfs(root.right,curSum)
            dfs(root.left,curSum)

            current_path.pop()
        dfs(root,0)
        return paths