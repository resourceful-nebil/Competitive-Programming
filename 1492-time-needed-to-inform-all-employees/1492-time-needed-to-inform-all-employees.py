class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)

        q = deque([(headID,0)]) # node,time
        res = 0

        #BFS
        while q:
            i, time = q.popleft()
            res = max(res,time)

            for nei in adj[i]:
                q.append((nei,time + informTime[i]))
        
        return res
