class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = list(range(len(strs)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for i in range(len(strs)):
            for j in range(i + 1,len(strs)):
                if sum(strs[i][k] != strs[j][k] for k in range(len(strs[0]))) <= 2:
                    parent[find(i)] = find(j)

        return sum(i == find(i) for i in range(len(strs)))