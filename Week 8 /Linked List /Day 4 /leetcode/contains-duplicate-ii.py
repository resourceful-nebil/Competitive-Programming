class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        numIndexOf = {}

        for i in range(n):
            if nums[i] in numIndexOf and i - numIndexOf[nums[i]] <= k:
                return True

            numIndexOf[nums[i]] = i

            if len(numIndexOf) > k:
                del numIndexOf[nums[i - k]]

        return False
        