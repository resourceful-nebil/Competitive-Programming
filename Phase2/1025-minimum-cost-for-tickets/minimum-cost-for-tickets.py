class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        nums = set(days)
        mx = max(days)

        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]

            if i > mx or i > 365:
                return 0
            if i not in nums:
                return dp(i + 1) 

            
            val = 0
            val = min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])

            memo[i] = val
            return val
        
        return dp(1)
            

