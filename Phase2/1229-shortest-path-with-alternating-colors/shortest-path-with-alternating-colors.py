class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(set)
        blue = defaultdict(set)

        for s,e in redEdges:
            red[s].add(e)
        
        for s,e in blueEdges:
            blue[s].add(e)

        # print(red,blue)
        answer = [-1 for _ in range(n)]
    
        q = deque()
        q.append([0,0,None])

        visited = set()
        visited.add((0,None))

        while q:
            # print(q)
            node,le,color = q.popleft()

            if answer[node] == -1:
                answer[node] = le
            
            if color != "RED":
                for nei in red[node]:
                    if (nei,"RED") not in visited:
                        visited.add((nei,"RED"))
                        q.append([nei,le + 1,"RED"])
            
            if color != "BLUE":
                for nei in blue[node]:
                    if (nei,"BLUE") not in visited:
                        visited.add((nei,"BLUE"))
                        q.append([nei,le + 1,"BLUE"])
        return answer   
                

