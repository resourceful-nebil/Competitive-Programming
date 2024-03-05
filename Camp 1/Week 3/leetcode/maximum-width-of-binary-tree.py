# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)

        def backtrack(root,level,levelCount):
            if not root:
                return 
            
            if root:
                di[level].append(levelCount)
                backtrack(root.left,level + 1,(2 * levelCount) + 1)
                backtrack(root.right,level + 1,(2 * levelCount) + 2)
        
        backtrack(root,0,0)
        ans = 0
        for key,value in di.items():
            ans = max(ans,value[-1] - value[0] + 1)
        return ans

            



            