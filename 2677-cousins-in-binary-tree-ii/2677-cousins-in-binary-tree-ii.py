# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(int)
        res = []
        queue = deque([root])
        while queue:
            tot = 0  
            for _ in range(len(queue)):
                node = queue.popleft()
                tot += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if node.left and node.right:
                    d[node.left] = node.right.val
                    d[node.right] = node.left.val

            res.append(tot)

        queue = deque([root])
        i = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                node.val = res[i] - node.val - d[node]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            i += 1

        return root

