class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        cnt = 0

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    visited.add(j)
                    dfs(j)
            
        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)
        
        return cnt