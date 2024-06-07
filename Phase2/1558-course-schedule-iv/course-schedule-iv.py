class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preGrid = [[False] * numCourses for _ in range(numCourses)]
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for pre,cor in prerequisites:
            graph[pre].append(cor)
            indeg[cor] += 1
        
        q = deque()
        for i,cnt in enumerate(indeg):
            if cnt == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                preGrid[node][nei] = True 

                for cur in range(numCourses):
                    preGrid[cur][nei] = preGrid[cur][nei] or preGrid[cur][node]

                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        res = []
        for i,f in queries:
            res.append(preGrid[i][f])
        
        return res 
        
