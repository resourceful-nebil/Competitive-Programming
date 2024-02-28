# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        di = defaultdict(int)

        def traverse(root):
            if root:
                di[root.val] += 1
                traverse(root.left)
                traverse(root.right)
                
        traverse(root)
            
        ans = []
        maxx = max(di.values())
        for i in di:
            if di[i] == maxx:
                ans.append(i)
        return ans


        