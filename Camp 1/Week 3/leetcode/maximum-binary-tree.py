# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(arr):
            if not arr:
                return None 
            
            mx = max(arr)
            i = arr.index(mx)

            left = dfs(arr[:i])
            right = dfs(arr[i+1:])

            return TreeNode(mx,left,right)
        
        return dfs(nums)