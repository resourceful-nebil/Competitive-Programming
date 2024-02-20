class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = patch = 0
        unreacheable = 1

        while unreacheable <= n:
            if i < len(nums) and unreacheable >= nums[i]:
                unreacheable += nums[i]
                i += 1
            else:
                unreacheable *= 2
                patch += 1
        return patch