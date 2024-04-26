class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {i : i for i in range(len(stones))}
        size = [1] * len(stones)
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
        
        for i in range(len(stones)):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        
        # print(root)
        cnt = 0
        for i,stone in enumerate(stones):
            if find(i) != i:
                cnt += 1
        
        return cnt
            
