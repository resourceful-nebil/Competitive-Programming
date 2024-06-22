class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], times: List[int]) -> int:
        graph = defaultdict(list)
        indeg = [0] * n
        for src,des in relations:
            graph[src - 1].append(des - 1)
            indeg[des - 1] += 1
        
        q = deque()
        finish_times = [0] * n
        max_time = 0
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                finish_times[i] = times[i]
                max_time = max(max_time,times[i])
        
        while q:
            current = q.popleft()
            for dependent in graph[current]:
                finish_times[dependent] = max(finish_times[dependent],finish_times[current] + times[dependent])
                max_time = max(max_time,finish_times[dependent])

                indeg[dependent] -= 1
                if indeg[dependent] == 0:
                    q.append(dependent)
        
        return max_time 
            