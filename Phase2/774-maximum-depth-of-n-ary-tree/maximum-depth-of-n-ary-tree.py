"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node):
            if node is None:
                return 0
            
            if not node.children:
                return 1
            
            max_depth = 0
            for child in node.children:
                child_depth = dfs(child)
                max_depth = max(max_depth,child_depth)
            
            return max_depth + 1
        
        return dfs(root)