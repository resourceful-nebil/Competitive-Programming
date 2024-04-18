class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        indegree = [0] * numCourses
        graph = defaultdict(set)

        for after,pre in prerequisites:
            graph[pre].add(after)
            indegree[after] += 1
        
        q = deque()
        for i,indeg in enumerate(indegree):
            if indegree[i] == 0:
                q.append(i)

        # print(q)
        while q:
            node = q.popleft()
            ans.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(ans) != numCourses:
            return [] 
        
        return ans

        
