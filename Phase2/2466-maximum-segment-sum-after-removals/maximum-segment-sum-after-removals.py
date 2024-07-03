class UnionFind:
    def __init__(self, size):
        self.ans = 0
        self.parent = {i:i for i in range(size)}
        self.size = [0 for _ in range(size)]
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
        
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        
        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                root1, root2 = root2, root1

            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
            self.ans = max(self.ans, self.size[root2])


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        res = []
        dsu = UnionFind(n)
  
        for i in removeQueries[::-1]:
            dsu.size[i] = nums[i]
            res.append(dsu.ans)
            if i > 0 and dsu.size[i - 1]:
                dsu.union(i, i - 1)

            if i < n - 1 and dsu.size[i + 1]:
                dsu.union(i, i + 1)

            dsu.ans = max(dsu.ans,nums[i])
            
        return res[::-1]