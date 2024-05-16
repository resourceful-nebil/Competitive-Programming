class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        cur = [1] + [0] * (n - 1)
        # print(prev)
        # print(cur)

        for i in range(m):
            for j in range(1,n ):
                cur[j] = prev[j] + cur[j-1]
            
            prev = cur
            cur = [1] + [0] * (n - 1)
        
        return prev[-1]