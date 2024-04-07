class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
    
        def bfs(node):
            if color[node]:
                return True

            queue = deque([node])
            color[node] = -1

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    # print(neighbor)
                    if color[neighbor] == color[node]:
                        # print(color[neighbor],'me')
                        return False
                    elif color[neighbor] == 0:
                        queue.append(neighbor)
                        color[neighbor] = -(color[node])
                    # elif color[neighbor] != 0:
                    #     continue
        
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True      
            




            