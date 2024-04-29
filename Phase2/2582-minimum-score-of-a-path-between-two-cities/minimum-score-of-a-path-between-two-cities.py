class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = {i : i for i in range(n)}
        size = [1] * (n)
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
        
        for road in roads:
            a,b,d = road
            union(b-1,a-1)
        
        # print(root)
        res = []
        for i,j,d in roads:
            # a,b,d = road
            if find(i-1) == find(0):
                res.append(d)

        # print(res)
        return min(res)
            