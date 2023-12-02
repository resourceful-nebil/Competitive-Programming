class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        size = len(nums)
        for i in range(0,size-1):
            for j in range(0,size):
                if nums[i] == nums[j] and i < j:
                    count +=1
        return count