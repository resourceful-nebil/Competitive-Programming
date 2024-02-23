class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx = 0
        div = 0

        for i in range(len(nums)):
            div += nums[i]
            val = ceil(div/(i+1)) 
            mx = max(mx,val)
        
        return mx

        
            