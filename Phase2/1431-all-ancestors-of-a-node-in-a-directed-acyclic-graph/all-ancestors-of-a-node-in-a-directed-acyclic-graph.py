class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        ancestor = [set() for _ in range(n)]
        indgree = [0] * n

        for fro, to in edges:
            graph[fro].add(to)
            indgree[to] += 1
        
        q = deque()
        for i in range(n):
            if indgree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()

            for nei in graph[node]:
                ancestor[nei].add(node)
                ancestor[nei] = ancestor[nei] | ancestor[node]
                # print(ancestor[nei],nei,ancestor[node],node)

                indgree[nei] -= 1
                if indgree[nei] == 0:
                    q.append(nei)
        
            
        return [sorted(anc) for anc in ancestor]

        