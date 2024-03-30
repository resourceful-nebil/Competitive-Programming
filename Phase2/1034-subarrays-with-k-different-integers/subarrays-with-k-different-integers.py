class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            count = 0
            left = 0
            di = defaultdict(int)
            for right in range(len(nums)):
                di[nums[right]] += 1
                while len(di) > k:
                    di[nums[left]] -= 1
                    if di[nums[left]] == 0:
                        del di[nums[left]]
                    left += 1
                count += right - left + 1
            return count

        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)