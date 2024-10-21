# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while q:
            current_level = []
            for node in q:
                current_level.append(node.val)

            res.append(current_level)

            next_level = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            q = next_level
                
        return res[::-1]
            

