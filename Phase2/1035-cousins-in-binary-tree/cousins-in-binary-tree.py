# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        prev = defaultdict(int)
        prev[root.val] = None

        def path(node):
            if node:
                if node.left:
                    prev[node.left.val] = node.val
                    path(node.left)
                if node.right:
                    prev[node.right.val] = node.val
                    path(node.right)
        path(root)
        arrx = []          
        while prev[x]:
            arrx.append(x)
            x = prev[x]
        arrx.append(root.val)
        
        arry = []          
        while prev[y]:
            arry.append(y)
            y = prev[y]
        arry.append(root.val)

        
        # print(arrx,arry)
 
        return len(arrx) == len(arry) and arrx[1] != arry[1]
        
        


            
            