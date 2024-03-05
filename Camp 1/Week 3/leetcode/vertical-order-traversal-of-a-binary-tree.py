# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        di = defaultdict(list)
        ans = []
        
        def dfs(root,row,col):
            if root:
                di[col].append((row,root.val))
                dfs(root.left,row + 1,col - 1)
                dfs(root.right,row + 1,col + 1)
            
        dfs(root,0,0)
        keys = list(di.keys())
        keys.sort()

        # row sort
        for val in di.values():
            val.sort()
        
        # to take the values from the dict
        for i in range(len(keys)):
            temp = []
            value = di[keys[i]]
            for row,val in value:
                temp.append(val)
            ans.append(temp)
        
        # print(di)
        return ans


