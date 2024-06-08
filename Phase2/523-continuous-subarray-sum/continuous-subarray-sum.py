class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first_occur =  {0: -1}
        # first_occur[0] = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum = (prefix_sum + nums[i]) % k
            if prefix_sum in first_occur:
                if (i - first_occur[prefix_sum]) >= 2:
                    return True
            else:
                first_occur[prefix_sum] = i 
        
        return False


        