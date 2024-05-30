class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        dp = defaultdict(int)
        n = len(nums)
        for i in range(n - 1,-1,-1):
            needed = nums[i] + difference

            dp[nums[i]] = 1 + dp[needed]
        
        mx = 0
        for key,val in dp.items():
            mx = max(mx,val)

        return mx

