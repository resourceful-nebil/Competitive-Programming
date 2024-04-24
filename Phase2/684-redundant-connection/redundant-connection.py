class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = len(edges) + 1
        root = {i:i for i in range(s)}
        size = [1] * s
        
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
        
        for x,y in edges:
            if find(x) == find(y):
                return [x,y]
            
            union(x,y)

        
        
                
                