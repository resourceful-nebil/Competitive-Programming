class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a,b in pairs:
            parent[find(a)] = find(b)

        d = defaultdict(list)

        for i,c in enumerate(s):
            d[find(i)].append(c)
        
        for c in d.values():
            c.sort(reverse=True)
        
        res = []
        for i in range(len(s)):
            res.append(d[find(i)].pop())
        
        return "".join(res)

        