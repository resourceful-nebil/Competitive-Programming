# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [inf,-inf]
            
            lmin,lmax = dfs(root.left)
            rmin, rmax = dfs(root.right)

            mn = min(lmin,rmin)
            mx = max(lmax,rmax)
            if root.right or root.left:
                diff = max(abs(root.val - mn),abs(root.val - mx))
                self.ans = max(self.ans,diff)

            return min(root.val,mn),max(root.val,mx)

        dfs(root)
        return self.ans
        