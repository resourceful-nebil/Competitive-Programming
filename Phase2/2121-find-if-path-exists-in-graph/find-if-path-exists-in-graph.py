class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i in range(len(edges)):
            s,e = edges[i]
            graph[s].append(e)
            graph[e].append(s)
        # print(graph)

        visited = set()


        def dfs(visited,vertex):
            if vertex == destination:
                return True 
            
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor in visited:
                    continue

                found = dfs(visited,neighbor)

                if found:
                    return True 
            
            return False

        

        return dfs(visited,source)