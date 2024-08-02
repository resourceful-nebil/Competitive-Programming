class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        return True if any(val > 1 for val in cnt.values()) else False
