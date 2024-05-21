class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(triangle):
                return 0
            
            res = min(triangle[i][j] + dp(i + 1,j),triangle[i][j] + dp(i + 1,j + 1))
            # print(res)
            memo[(i,j)] = res
            return res  
        
        return dp(0,0)

