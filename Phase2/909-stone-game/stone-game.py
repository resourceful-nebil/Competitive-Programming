class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dp(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l > r:
                return 0
            
            even = True if (r - 1) % 2 else 0
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            val = -float('inf')
            val = max(dp(l,r-1) + right, dp(l + 1,r) + left)

            memo[(l,r)] = val
            return val
        
        return dp(0, len(piles) - 1) > sum(piles) // 2