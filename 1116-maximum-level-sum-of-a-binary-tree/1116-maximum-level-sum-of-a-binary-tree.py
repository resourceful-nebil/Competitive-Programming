# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level = 0
        largest = float('-inf')
        ans = 0

        if root:
            q.append(root)

        while q:
            curSum = 0
            for i in range(len(q)):
                curNode = q.popleft()

                curSum += curNode.val

                if curNode.right:
                    q.append(curNode.right)
                if curNode.left:
                    q.append(curNode.left)
            level += 1
            if curSum > largest:
                ans = level
            largest = max(largest,curSum)
        return ans