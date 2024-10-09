class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = []

        def dfs(i):
            path.append(i)
            if i == len(graph) - 1:
                paths.append(path[:]) 
            else:
                for nei in graph[i]:
                    dfs(nei)
            
            path.pop()

        dfs(0)
        return paths