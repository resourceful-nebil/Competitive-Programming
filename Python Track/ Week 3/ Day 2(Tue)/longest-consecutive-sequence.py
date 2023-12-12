class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in nums:
            
            # check if it is the begining of the sequence
            if (num - 1) not in numsSet:
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longest = max(length,longest)
        return longest 
                
    """  
        # 2nd approach  
        nums.sort()
        res = 0
        current_len = 1

        for i in range(1,len(nums)-1):
            if nums[i] == nums[i-1] + 1:
                current_len += 1
            else:
                res = max(res,current_len)
                current_len = 1

        res = max(res,current_len)
        return res 
"""


    '''  
        # First approach   
        nums.sort()
        res = 0


        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                current_len += 1
        
        return res
        
    '''