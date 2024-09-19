# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []

        if root:
            q.append(root)
        
        while q:
            level_size = len(q)  # Number of nodes at the current level
            for i in range(level_size):
                cur = q.popleft()

                # Only append the rightmost node of the level to ans
                if i == level_size - 1:
                    ans.append(cur.val)

                # Add left and right children to the queue
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return ans
                