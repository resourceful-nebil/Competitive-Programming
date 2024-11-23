class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,res = 0,0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                res = max(res,prof)
            else:
                l = r
            
        return res 