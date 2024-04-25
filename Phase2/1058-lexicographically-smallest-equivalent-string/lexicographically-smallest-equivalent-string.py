class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {chr(i) : chr(i) for i in range(97,124)}

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if ord(rootX) > ord(rootY):
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
            
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        res = []
        for i in range(len(baseStr)):
            res.append(find(baseStr[i]))
        
        
        return ''.join(res)