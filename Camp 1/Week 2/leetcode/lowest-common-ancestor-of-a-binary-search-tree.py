# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root,node):
            if not root:
                return []
            
            if root.val == node.val:
                return [root]

            if root.val > node.val:
                ans = []
                ans.append(root)
                ans.extend(lca(root.left, node))
            else:
                ans = []
                ans.append(root)
                ans.extend(lca(root.right, node))
            return ans
            
        parr = lca(root,p)
        qarr = lca(root,q)
        

        i = max(len(parr) - 1,len(qarr) - 1) 
        # print(i)
        # print(len(parr),len(qarr))
        while i > -1:
            if i < len(parr) and i < len(qarr):
                print(parr[i].val ,qarr[i].val)
                if parr[i] == qarr[i]:
                    return parr[i] 
            i -= 1

        


            

