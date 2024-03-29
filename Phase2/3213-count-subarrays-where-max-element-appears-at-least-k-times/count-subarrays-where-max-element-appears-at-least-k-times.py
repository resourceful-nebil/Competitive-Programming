class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        target = max(nums)
        di = defaultdict(int)

        left = 0
        for right in range(len(nums)):
            di[nums[right]] += 1

            while di[target] >= k:
                count += (len(nums) - right)
                di[nums[left]] -= 1
                left += 1
  

        return count 