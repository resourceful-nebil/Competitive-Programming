class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        prof = 0
        for n in prices:
            if n < mn:
                mn = n
            else:
                prof = max(n - mn, prof)
        return prof