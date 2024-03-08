# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        def dfs(root):
            if root:
                dfs(root.left)
                nums.append(root.val)
                dfs(root.right)
        dfs(root)
        # print(nums)   
        def makeBst(left,right):
            if left > right:
                return None
            
            mid = (left + right)//2

            # root = TreeNode(arr[mid])
            left= makeBst(left,mid - 1)
            right= makeBst(mid + 1,right)

            return TreeNode(nums[mid],left,right)

        return makeBst(0,len(nums) - 1)
