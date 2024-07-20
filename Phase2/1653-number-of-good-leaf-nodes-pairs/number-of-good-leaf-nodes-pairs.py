# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root is None:
            return 0
        
        total = self.countPairs(root.left,distance) + self.countPairs(root.right,distance) 
        left_count = Counter()
        right_count = Counter()

        def dfs(node,leaf_count,i):
            if not node:
                return 
            if node.left is None and node.right is None:
                leaf_count[i] += 1
                return
            
            dfs(node.left,leaf_count,i + 1)
            dfs(node.right,leaf_count,i + 1)
        

        dfs(root.left,left_count,1)
        dfs(root.right,right_count,1)

        for depth_left, count_left in left_count.items():
            for depth_right, count_right in right_count.items():
                if depth_left + depth_right <= distance:
                    total += count_left * count_right
        return total


