class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prefix = 1
        suffix_arr = [1]*(len(nums))
        suffix = 1
        

        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            ans[i] = prefix
        
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix = 1
            else:
                suffix *= nums[i+1]
            suffix_arr[i] = suffix
            ans[i] *= suffix_arr[i]
            
        return ans
            
        