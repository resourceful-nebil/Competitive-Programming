class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x !=  y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

        

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        #build components
        uf = UnionFind(n)
        print(uf.parent,uf.size)
        for u,v,w in edges:
            uf.union(u,v)
        
        #get cost
        cost = {}
        for u,v,w in edges:
            root = uf.find(u)
            if root not in cost:
                cost[root] = w
            else:
                cost[root] &= w
        
        print(cost,uf.parent,uf.size)
        
        #query
        res = []
        for q1,q2 in query:
            r1 = uf.find(q1)
            r2 = uf.find(q2)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(cost[r1])
            
        return res
