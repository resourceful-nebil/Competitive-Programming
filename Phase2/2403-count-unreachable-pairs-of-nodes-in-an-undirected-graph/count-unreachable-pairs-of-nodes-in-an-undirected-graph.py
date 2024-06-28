class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for src,des in edges:
            graph[src].append(des)
            graph[des].append(src)
        
        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)

            total = 1
            for nei in graph[node]:
                total += dfs(nei)
            
            return total

        ans, s = 0, 0
        for i in range(n):
            t = dfs(i)
            ans += (s * t)
            s += t
        
        return ans 
