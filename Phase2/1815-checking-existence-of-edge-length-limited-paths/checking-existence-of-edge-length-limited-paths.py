class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]

        def find(x):  
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def Union(x, y):  
            x = find(x)
            y = find(y)
            parent[x] = y

        for i in range(len(queries)):  
            queries[i].append(i)
        queries.sort(key = lambda x: x[2])
        edgeList.sort(key = lambda x: x[2])
        
        i = 0
        ans = [False for j in range(len(queries))]
        for query in queries:
            limit = query[2]
            while (i < len(edgeList) and edgeList[i][2] < limit): 
                u = edgeList[i][0]
                v = edgeList[i][1]
                Union(u, v)
                i += 1
            p = query[0]
            q = query[1]
            queryIndex = query[3]
            if find(p) == find(q):  # checks if p and q are connected
                ans[queryIndex] = True
        return ans 
        
        
