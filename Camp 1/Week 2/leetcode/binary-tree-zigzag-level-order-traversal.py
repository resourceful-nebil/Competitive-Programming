# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        height = 0
        zigzag = defaultdict(list)

        def dfs(root,height):
            if not root:
                return 
            
            if root:
                zigzag[height].append(root.val)
                dfs(root.left,height + 1)
                dfs(root.right,height + 1)

        dfs(root,height)
        # print(zigzag)
        ans = []
        sorted_zigzag = dict(sorted(zigzag.items()))
        # print(sorted_zigzag)

        flag = False
        for value in sorted_zigzag.values():
            if flag:
                ans.append(value[::-1])
            else:
                ans.append(value)
            flag = not flag

        return ans

