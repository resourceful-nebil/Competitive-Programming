class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[j] == -nums[i]:
                return nums[j]
            
            if nums[j] > -nums[i]:
                j -= 1
            else:
                i += 1
                

        return -1