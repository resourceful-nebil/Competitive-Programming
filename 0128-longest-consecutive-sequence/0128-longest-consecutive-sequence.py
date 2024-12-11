class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
       
        res = 0
        curr_len = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_len += 1
            elif  nums[i] == nums[i - 1]:
                continue
            else:
                res = max(res, curr_len)
                curr_len = 1
        
        res = max(res, curr_len)
        return res if nums else 0