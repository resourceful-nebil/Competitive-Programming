class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #dfs
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(i):
            visited[i] = True 
            for j in range(len(isConnected)):
                if not visited[j] and isConnected[i][j] == 1:
                    visited[j] = True
                    dfs(j)


        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count 
