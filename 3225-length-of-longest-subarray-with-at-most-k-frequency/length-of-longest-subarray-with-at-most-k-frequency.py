class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        max_length = 0
        di = defaultdict(int)
        left = 0

        for i in range(len(nums)):
            di[nums[i]] += 1

            while di[nums[i]] > k:
                di[nums[left]] -= 1
                left += 1
            
            max_length = max(max_length,i - left + 1)
        
        return max_length


