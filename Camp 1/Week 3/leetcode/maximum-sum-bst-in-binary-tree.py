# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        def dfs(root):
            ans = [True,float('-inf'),float('inf'),root.val]
            
            # for leaf nodes
            if not root.left and not root.right:
                ans[1] = root.val
                ans[2] = root.val
            
            # for left subtrees
            if root.left:
                temp = dfs(root.left)
                ans[0] = temp[0] and (root.val > temp[1])
                ans[1] = max(root.val,temp[1])
                ans[2] = min(root.val,temp[2])
                ans[3] += temp[3]
            
            # for right subtrees
            if root.right:
                temp = dfs(root.right)
                ans[0] = temp[0] and ans[0] and (root.val < temp[2])
                ans[1] = max(ans[1],temp[1],root.val)
                ans[2] = min(ans[2],temp[2],root.val)
                ans[3] += temp[3]

            # to append in our check if the returned value is True
            if ans[0]:
                res.append(ans[3])

            return ans
        
        dfs(root)
        return max(res)
            


