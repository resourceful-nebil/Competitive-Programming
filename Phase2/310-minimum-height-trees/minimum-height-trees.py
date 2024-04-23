class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]    
        
        graph = defaultdict(list)
        for src,des in edges:
            graph[src].append(des)
            graph[des].append(src)
        
        edge_cnt = {}
        q = deque()
        for src, nei in graph.items():
            if len(nei) == 1:
                q.append(src)
            edge_cnt[src] = len(nei)
        
        while q:
            if n <= 2:
                return list(q)

            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in graph[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        q.append(nei)
