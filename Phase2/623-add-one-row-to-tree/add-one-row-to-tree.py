# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newTree = TreeNode(val)
            newTree.left = root
            return newTree

        def dfs(node,level):
            if node:
                if level == depth - 1:
                    if node.left:
                        tmp = node.left
                        node.left = TreeNode(val)
                        node.left.left = tmp
                    else:
                        new = TreeNode(val)
                        node.left = new
                    if node.right:
                        tmp = node.right
                        node.right = TreeNode(val)
                        node.right.right = tmp
                    else:
                        new = TreeNode(val)
                        node.right = new
                if node.left:
                    dfs(node.left,level + 1)
                if node.right:
                    dfs(node.right,level + 1)
        
        dfs(root,1)

        return root