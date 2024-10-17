class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjancy list 
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        cnt = 0

        while q:
            course = q.popleft()
            cnt += 1
            
            for nei in graph[course]:
                indegree[nei] -= 1
            
                if indegree[nei] == 0:
                    q.append(nei)
            
        return cnt == numCourses



        
        



        
