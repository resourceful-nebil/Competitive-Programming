class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,av = 0, float('-inf')
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            if r - l + 1 == k:
                av = max(av,total)
                total -= nums[l]
                l += 1
            
        return av/k
