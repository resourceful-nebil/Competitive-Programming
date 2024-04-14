# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = []

        def traverse(node):
            if node:
                if node.left:
                    if not node.left.left and not node.left.right:
                        left_sum.append(node.left.val)
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
        
        traverse(root)
        # print(left_sum)
        return sum(left_sum)
