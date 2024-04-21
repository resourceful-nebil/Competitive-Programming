# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)

        def traverse(node):
            if node:
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val].add(node.val)
                    traverse(node.left)
                if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val].add(node.val)
                    traverse(node.right)
        traverse(root)   
        # print(graph)

        q = deque()
        q.append([target.val,0])

        visited = set()
        visited.add(target.val)

        res = []
        while q:
            # print(q)
            for _ in range(len(q)):
                node, level = q.popleft()

                if level == k:
                    res.append(node)
                
                for nei in graph[node]:
                    if nei not in visited:
                        q.append([nei,level + 1])
                        visited.add(nei)
        
        return res
                



